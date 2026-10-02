"""
FastAPI Backend Application for Care Chronicle.
Outpatient Assistive Oncology System designed for Healthathon 2026.
Strictly non-diagnostic, workflow-first, human-in-the-loop.
"""

import os
from typing import List, Dict, Any, Optional
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .models import (
    PatientProfile,
    ClinicalDocument,
    TimelineEvent,
    DeltaSummary,
    AdministrativeTask,
    AuditLogEntry,
    VoiceMemoRequest,
    VoiceMemoResponse,
    IngestionResponse,
    PatientHistoryArchive
)
from .synthetic_data import (
    PATIENTS_DATA,
    DOCUMENTS_DATA,
    TIMELINE_DATA,
    DELTA_SUMMARIES,
    ADMIN_TASKS,
    AUDIT_LOGS,
    PATIENT_HISTORIES
)
from .ocr_parser import DocumentParserEngine
from .orchestration import (
    execute_ingestion_pipeline,
    VoiceTaskExtractorAgent
)
from .translations import TRANSLATIONS

app = FastAPI(
    title="Care Chronicle API",
    description="Assistive Outpatient Oncology Workflow Assistant",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory working state cloned from synthetic templates
state_patients: Dict[str, PatientProfile] = {k: v.model_copy() for k, v in PATIENTS_DATA.items()}
state_documents: Dict[str, List[ClinicalDocument]] = {k: [d.model_copy() for d in v] for k, v in DOCUMENTS_DATA.items()}
state_timelines: Dict[str, List[TimelineEvent]] = {k: [e.model_copy() for e in v] for k, v in TIMELINE_DATA.items()}
state_deltas: Dict[str, DeltaSummary] = {k: v.model_copy() for k, v in DELTA_SUMMARIES.items()}
state_tasks: Dict[str, List[AdministrativeTask]] = {k: [t.model_copy() for t in v] for k, v in ADMIN_TASKS.items()}
state_audit_logs: Dict[str, List[AuditLogEntry]] = {k: [a.model_copy() for a in v] for k, v in AUDIT_LOGS.items()}
state_histories: Dict[str, PatientHistoryArchive] = {k: v.model_copy() for k, v in PATIENT_HISTORIES.items()}

# Chart review timer session trackers
chart_review_sessions: Dict[str, Dict[str, Any]] = {}

@app.get("/api/patients", response_model=List[PatientProfile])
def get_all_patients():
    """Returns the list of all synthetic patient profiles."""
    return list(state_patients.values())

@app.get("/api/patient/{patient_id}")
def get_patient_detail(patient_id: str):
    """Returns complete longitudinal record and active dashboard context for a patient."""
    if patient_id not in state_patients:
        raise HTTPException(status_code=404, detail="Patient profile not found")

    return {
        "profile": state_patients[patient_id],
        "delta": state_deltas.get(patient_id),
        "documents": state_documents.get(patient_id, []),
        "timeline": state_timelines.get(patient_id, []),
        "tasks": state_tasks.get(patient_id, []),
        "audit_logs": state_audit_logs.get(patient_id, []),
        "history": state_histories.get(patient_id)
    }

@app.post("/api/patient/{patient_id}/ingest-sample", response_model=IngestionResponse)
def ingest_sample_document(patient_id: str, sample_type: str = "cbc_panel"):
    """
    Ingests one of the pre-configured clinical sample templates
    (e.g., ct_scan, histopathology, cbc_panel) through the LangGraph pipeline.
    """
    if patient_id not in state_patients:
        raise HTTPException(status_code=404, detail="Patient not found")

    patient = state_patients[patient_id]
    new_doc = DocumentParserEngine.parse_sample(sample_type, patient_id)

    # Run multi-agent LangGraph ingestion pipeline
    res = execute_ingestion_pipeline(
        patient_id=patient_id,
        patient_name=patient.name,
        document=new_doc,
        previous_delta=state_deltas.get(patient_id)
    )

    processed_doc = res["document"]
    updated_delta = res["updated_delta"]
    audit_entry = res["audit_entry"]
    timeline_evt = res["timeline_event"]

    # Commit to state
    if patient_id not in state_documents:
        state_documents[patient_id] = []
    state_documents[patient_id].insert(0, processed_doc)

    if updated_delta:
        state_deltas[patient_id] = updated_delta

    if audit_entry:
        if patient_id not in state_audit_logs:
            state_audit_logs[patient_id] = []
        state_audit_logs[patient_id].insert(0, audit_entry)

    if timeline_evt:
        if patient_id not in state_timelines:
            state_timelines[patient_id] = []
        state_timelines[patient_id].insert(0, timeline_evt)

    return IngestionResponse(
        success=True,
        message=f"Successfully processed and indexed {processed_doc.title}",
        document=processed_doc,
        updated_delta=updated_delta or state_deltas[patient_id],
        new_audit_entry=audit_entry,
        added_timeline_event=timeline_evt
    )

@app.post("/api/patient/{patient_id}/upload-document", response_model=IngestionResponse)
async def upload_document(patient_id: str, file: UploadFile = File(...)):
    """Uploads a clinical document and passes it to the LangGraph parsing graph."""
    if patient_id not in state_patients:
        raise HTTPException(status_code=404, detail="Patient not found")

    contents = await file.read()
    new_doc = DocumentParserEngine.parse_uploaded_file(file.filename, contents, patient_id)

    patient = state_patients[patient_id]
    res = execute_ingestion_pipeline(
        patient_id=patient_id,
        patient_name=patient.name,
        document=new_doc,
        previous_delta=state_deltas.get(patient_id)
    )

    processed_doc = res["document"]
    updated_delta = res["updated_delta"]
    audit_entry = res["audit_entry"]
    timeline_evt = res["timeline_event"]

    if patient_id not in state_documents:
        state_documents[patient_id] = []
    state_documents[patient_id].insert(0, processed_doc)

    if updated_delta:
        state_deltas[patient_id] = updated_delta

    if audit_entry:
        if patient_id not in state_audit_logs:
            state_audit_logs[patient_id] = []
        state_audit_logs[patient_id].insert(0, audit_entry)

    if timeline_evt:
        if patient_id not in state_timelines:
            state_timelines[patient_id] = []
        state_timelines[patient_id].insert(0, timeline_evt)

    return IngestionResponse(
        success=True,
        message=f"Document '{file.filename}' parsed and normalized successfully.",
        document=processed_doc,
        updated_delta=updated_delta or state_deltas[patient_id],
        new_audit_entry=audit_entry,
        added_timeline_event=timeline_evt
    )

@app.get("/api/patient/{patient_id}/sample-voice-memo")
def get_sample_voice_memo(patient_id: str):
    """Returns the realistic clinician voice memo fallback text for one-click testing."""
    memo = VoiceTaskExtractorAgent.get_sample_memo(patient_id)
    return {"patient_id": patient_id, "sample_memo": memo}

@app.post("/api/patient/{patient_id}/voice-memo", response_model=VoiceMemoResponse)
def process_voice_memo(patient_id: str, payload: VoiceMemoRequest):
    """
    Parses doctor consultation audio transcript using the LangChain task agent
    and logs actionable tasks and audit records.
    """
    if patient_id not in state_patients:
        raise HTTPException(status_code=404, detail="Patient not found")

    transcript = payload.transcript.strip()
    if not transcript:
        raise HTTPException(status_code=400, detail="Transcript cannot be empty")

    new_tasks = VoiceTaskExtractorAgent.extract_tasks_from_memo(patient_id, transcript)
    audit_entry = VoiceTaskExtractorAgent.create_audit_entry_for_voice(patient_id, transcript, len(new_tasks))

    # Prepend new tasks to patient task checklist
    if patient_id not in state_tasks:
        state_tasks[patient_id] = []
    for t in reversed(new_tasks):
        state_tasks[patient_id].insert(0, t)

    # Log to audit trail
    if patient_id not in state_audit_logs:
        state_audit_logs[patient_id] = []
    state_audit_logs[patient_id].insert(0, audit_entry)

    return VoiceMemoResponse(
        success=True,
        transcript=transcript,
        extracted_tasks=new_tasks,
        audit_entry=audit_entry
    )

class TaskToggleRequest(BaseModel):
    completed: bool

@app.post("/api/tasks/{task_id}/toggle")
def toggle_task(task_id: str, payload: TaskToggleRequest):
    """Toggles completion status for an administrative action item."""
    for p_id, tasks in state_tasks.items():
        for t in tasks:
            if t.id == task_id:
                t.completed = payload.completed
                return {"success": True, "task_id": task_id, "completed": t.completed}
    raise HTTPException(status_code=404, detail="Task not found")

class NewTaskPayload(BaseModel):
    patient_id: str
    title: str
    category: str = "Administrative"
    priority: str = "Standard"

@app.post("/api/tasks/add")
def add_new_task(payload: NewTaskPayload):
    """Clinician manual addition of an administrative task."""
    import uuid
    new_t = AdministrativeTask(
        id=f"TSK-MAN-{uuid.uuid4().hex[:5].upper()}",
        patient_id=payload.patient_id,
        title=payload.title,
        category=payload.category,
        completed=False,
        priority=payload.priority,
        due_info="Added manually"
    )
    if payload.patient_id not in state_tasks:
        state_tasks[payload.patient_id] = []
    state_tasks[payload.patient_id].insert(0, new_t)
    return {"success": True, "task": new_t}

@app.post("/api/audit/{log_id}/verify")
def verify_audit_entry(log_id: str):
    """Clinician verification sign-off on an automated AI agent action."""
    for p_id, logs in state_audit_logs.items():
        for l in logs:
            if l.id == log_id:
                l.status = "Verified"
                return {"success": True, "log_id": log_id, "status": l.status}
    raise HTTPException(status_code=404, detail="Audit log entry not found")

class ChartReviewFinishRequest(BaseModel):
    duration_seconds: int

@app.post("/api/patient/{patient_id}/finish-chart-review")
def finish_chart_review(patient_id: str, payload: ChartReviewFinishRequest):
    """Records that the doctor finished chart review and tracks Prep Time KPI."""
    if patient_id not in state_patients:
        raise HTTPException(status_code=404, detail="Patient not found")

    chart_review_sessions[patient_id] = {
        "duration_seconds": payload.duration_seconds,
        "completed": True
    }
    return {
        "success": True,
        "patient_id": patient_id,
        "review_duration": payload.duration_seconds,
        "target_met": payload.duration_seconds < 60,
        "message": f"Chart review completed in {payload.duration_seconds}s (Target: < 60s)"
    }

@app.get("/api/translations")
def get_translations():
    """Returns UI chrome translation dictionaries."""
    return TRANSLATIONS

# Serve frontend static assets
STATIC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "static"))
if os.path.exists(STATIC_DIR):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/")
def serve_index():
    index_path = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return JSONResponse({"message": "Care Chronicle API is active. Static files loading."})
