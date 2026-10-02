from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class ClinicalTableRow(BaseModel):
    parameter: str
    value: str
    unit: str = ""
    reference_range: str = ""
    flag: str = "Normal"  # "Normal", "Low", "High", "Critical"
    notes: Optional[str] = ""

class ClinicalDocument(BaseModel):
    id: str
    patient_id: str
    title: str
    category: str  # "CT Abdomen Scan", "Histopathology Report", "CBC Blood Panel", etc.
    date: str
    facility: str = "Celabs Diagnostics Pvt. Ltd."
    accreditation: str = "NABL & CAP Certified | ISO 15189:2022"
    specimen_id: Optional[str] = "SPEC-89210-B"
    summary: str
    clinical_notes: str = ""
    table_data: List[ClinicalTableRow] = Field(default_factory=list)
    findings: List[str] = Field(default_factory=list)
    conclusion: str
    reporting_specialist: str = "Dr. S. K. Mehta, MD (Pathology / Radiodiagnosis)"
    source_file_name: str
    file_size: str
    status: str = "Indexed"

class TimelineEvent(BaseModel):
    id: str
    patient_id: str
    date: str
    event_type: str  # "Chemo", "Scans", "Surgery", "Visit"
    title: str
    subtitle: str
    description: str
    badge: str
    metrics: Dict[str, str] = Field(default_factory=dict)
    status: str = "Completed"

class DeltaSummary(BaseModel):
    patient_id: str
    headline: str
    points: List[str]
    last_compared_date: str
    impact_level: str = "Stable"

class AdministrativeTask(BaseModel):
    id: str
    patient_id: str
    title: str
    category: str
    completed: bool = False
    priority: str = "Standard"
    due_info: str = "Within 48 hours"

class AuditLogEntry(BaseModel):
    id: str
    patient_id: str
    timestamp: str
    agent_action: str
    source_document: str
    parameters_extracted: List[str]
    confidence_metric: str = "High (Human Review Ready)"
    status: str = "Pending Review"  # "Pending Review" or "Verified"
    traceability_details: Dict[str, Any] = Field(default_factory=dict)

class SerialLabTrend(BaseModel):
    parameter: str
    baseline: str
    interim: str
    current: str
    reference_range: str
    trend_status: str  # "Favorable", "Stable", "Monitoring"

class ArchivedVoiceMemo(BaseModel):
    id: str
    encounter_date: str
    treating_oncologist: str
    audio_duration: str
    transcript: str
    action_items_count: int

class PatientHistoryArchive(BaseModel):
    patient_id: str
    diagnosis_anchor_date: str
    primary_surgery_summary: str
    total_chemo_cycles_delivered: str
    radiation_summary: Optional[str] = "None (Systemic Protocol)"
    serial_lab_trends: List[SerialLabTrend] = Field(default_factory=list)
    stored_voice_memos: List[ArchivedVoiceMemo] = Field(default_factory=list)
    key_historical_milestones: List[Dict[str, str]] = Field(default_factory=list)

class PatientProfile(BaseModel):
    id: str
    name: str
    age: int
    gender: str
    medical_record_number: str
    diagnosis: str
    stage: str
    regimen: str
    current_cycle: str
    cycle_current: int = 1
    cycle_total: int = 12
    milestone_headline: str = ""
    milestone_date: str = ""
    next_restaging_milestone: str = ""
    baseline_prep_time_sec: int
    handoff_lag_reduction_min: float
    treating_physician: str
    hospital_name: str = "National Comprehensive Cancer Institute"
    last_visit_date: str
    next_scheduled_date: str

class IngestionResponse(BaseModel):
    success: bool
    message: str
    document: ClinicalDocument
    updated_delta: DeltaSummary
    new_audit_entry: AuditLogEntry
    added_timeline_event: Optional[TimelineEvent] = None

class VoiceMemoRequest(BaseModel):
    patient_id: str
    transcript: str

class VoiceMemoResponse(BaseModel):
    success: bool
    transcript: str
    extracted_tasks: List[AdministrativeTask]
    audit_entry: AuditLogEntry
