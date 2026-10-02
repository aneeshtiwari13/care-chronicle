"""
Synthetic Medical Records for Care Chronicle Oncology Outpatient Assistant.
All records are 100% synthetic, anonymized, and designed for demonstration of
clinician-assistive timeline synthesis, delta comparison, and handoff tracking.
"""

from typing import Dict, List
from .models import (
    PatientProfile,
    ClinicalDocument,
    ClinicalTableRow,
    TimelineEvent,
    DeltaSummary,
    AdministrativeTask,
    AuditLogEntry,
    PatientHistoryArchive,
    SerialLabTrend,
    ArchivedVoiceMemo
)

PATIENTS_DATA: Dict[str, PatientProfile] = {
    "P001": PatientProfile(
        id="P001",
        name="Rajesh Sharma",
        age=58,
        gender="Male",
        medical_record_number="SYN-ONC-8812",
        diagnosis="Stage IIIB Sigmoid Colon Adenocarcinoma (pT3N2aM0, MSS)",
        stage="Stage IIIB (Post-Resection)",
        regimen="Adjuvant mFOLFOX6 (Oxaliplatin, Leucovorin, 5-FU)",
        current_cycle="Cycle 3 of 12 (Scheduled for Tomorrow)",
        cycle_current=3,
        cycle_total=12,
        milestone_headline="Cycle 3 of 12 (mFOLFOX-6 Infusion)",
        milestone_date="03-Oct-2026 • Scheduled for Tomorrow at 08:30 AM",
        next_restaging_milestone="Post-Cycle 4 CT Restaging on 24-Oct-2026",
        baseline_prep_time_sec=51,
        handoff_lag_reduction_min=2.4,
        treating_physician="Dr. Arvind V. Kulkarni, MD, DM (Medical Oncology)",
        hospital_name="Apex Oncology Institute & Research Centre",
        last_visit_date="18-Sep-2026",
        next_scheduled_date="02-Oct-2026"
    ),
    "P002": PatientProfile(
        id="P002",
        name="Anita Devi",
        age=52,
        gender="Female",
        medical_record_number="SYN-ONC-9421",
        diagnosis="Invasive Ductal Carcinoma Left Breast (Grade 2, ER 90%, PR 75%, HER2 Negative)",
        stage="Stage IIA (cT2N0M0)",
        regimen="Dose-Dense AC followed by Paclitaxel (AC-T)",
        current_cycle="Cycle 2 of 4 (Doxorubicin + Cyclophosphamide)",
        cycle_current=2,
        cycle_total=4,
        milestone_headline="Cycle 2 of 4 (Dose-Dense AC Infusion)",
        milestone_date="04-Oct-2026 • Scheduled in 2 Days at 09:00 AM",
        next_restaging_milestone="Cardiac LVEF Echo Surveillance on 15-Nov-2026",
        baseline_prep_time_sec=44,
        handoff_lag_reduction_min=1.9,
        treating_physician="Dr. Meenakshi Sundaram, MD (Breast Medical Oncology)",
        hospital_name="Apex Oncology Institute & Research Centre",
        last_visit_date="20-Sep-2026",
        next_scheduled_date="04-Oct-2026"
    ),
    "P003": PatientProfile(
        id="P003",
        name="Vikram Singh",
        age=64,
        gender="Male",
        medical_record_number="SYN-ONC-7230",
        diagnosis="Non-Small Cell Lung Adenocarcinoma (EGFR Exon 21 L858R Mutation)",
        stage="Stage IV (Bilateral Pulmonary Nodules, No Bone/Brain Mets)",
        regimen="Targeted First-Line Osimertinib 80mg Oral Daily",
        current_cycle="Month 3 Maintenance Evaluation",
        cycle_current=3,
        cycle_total=12,
        milestone_headline="Month 3 of 12 (Targeted Osimertinib Maintenance)",
        milestone_date="03-Oct-2026 • Scheduled for Tomorrow at 11:00 AM",
        next_restaging_milestone="6-Month Restaging CT Chest & Brain MRI on 15-Dec-2026",
        baseline_prep_time_sec=58,
        handoff_lag_reduction_min=2.8,
        treating_physician="Dr. Arvind V. Kulkarni, MD, DM (Medical Oncology)",
        hospital_name="Apex Oncology Institute & Research Centre",
        last_visit_date="12-Sep-2026",
        next_scheduled_date="03-Oct-2026"
    ),
    "P004": PatientProfile(
        id="P004",
        name="Priya Nair",
        age=46,
        gender="Female",
        medical_record_number="SYN-ONC-6314",
        diagnosis="High-Grade Serous Carcinoma of Ovary / Peritoneum (BRCA1/2 Wildtype)",
        stage="Stage IIIC (Optimal Interval Debulking Performed)",
        regimen="Carboplatin AUC 5 + Paclitaxel 175mg/m² + Bevacizumab 15mg/kg",
        current_cycle="Cycle 4 of 6 (Adjuvant)",
        cycle_current=4,
        cycle_total=6,
        milestone_headline="Cycle 4 of 6 (Carbo-Taxol + Bevacizumab)",
        milestone_date="05-Oct-2026 • Scheduled for Monday at 08:30 AM",
        next_restaging_milestone="Post-Cycle 6 Restaging PET-CT on 18-Nov-2026",
        baseline_prep_time_sec=47,
        handoff_lag_reduction_min=2.1,
        treating_physician="Dr. Radhika Sen, MD, DNB (Gynecologic Oncology)",
        hospital_name="Apex Oncology Institute & Research Centre",
        last_visit_date="15-Sep-2026",
        next_scheduled_date="05-Oct-2026"
    ),
    "P005": PatientProfile(
        id="P005",
        name="Mohammed Al-Farsi",
        age=61,
        gender="Male",
        medical_record_number="SYN-ONC-5192",
        diagnosis="Multiple Myeloma (IgG Kappa Light Chain Restriced, Standard Cytogenetic Risk)",
        stage="ISS Stage II (R-ISS II)",
        regimen="VRd Regimen (Bortezomib SubQ, Lenalidomide Oral, Dexamethasone)",
        current_cycle="Cycle 4 Day 1 Evaluation",
        cycle_current=4,
        cycle_total=4,
        milestone_headline="Cycle 4 of 4 (VRd Induction Phase Completion)",
        milestone_date="03-Oct-2026 • Scheduled for Tomorrow at 10:00 AM",
        next_restaging_milestone="Stem Cell Transplant (BMT) Harvest on 14-Oct-2026",
        baseline_prep_time_sec=53,
        handoff_lag_reduction_min=2.5,
        treating_physician="Dr. Arvind V. Kulkarni, MD, DM (Medical Oncology)",
        hospital_name="Apex Oncology Institute & Research Centre",
        last_visit_date="10-Sep-2026",
        next_scheduled_date="02-Oct-2026"
    )
}

PATIENT_HISTORIES: Dict[str, PatientHistoryArchive] = {
    "P001": PatientHistoryArchive(
        patient_id="P001",
        diagnosis_anchor_date="12-Jul-2026",
        primary_surgery_summary="Laparoscopic Anterior Resection of Sigmoid Colon (24-Jul-2026). R0 Curative Resection, 21 lymph nodes harvested (3 positive, pT3N1bM0). Negative margins > 5cm.",
        total_chemo_cycles_delivered="2 of 12 Cycles Delivered (Adjuvant mFOLFOX-6)",
        radiation_summary="None (Systemic Adjuvant Protocol Indicated)",
        serial_lab_trends=[
            SerialLabTrend(parameter="Serum CEA (Carcinoembryonic Ag)", baseline="6.4 ng/mL", interim="3.9 ng/mL", current="2.8 ng/mL", reference_range="< 3.0 ng/mL", trend_status="Favorable"),
            SerialLabTrend(parameter="Platelet Count", baseline="240,000 /µL", interim="162,000 /µL", current="138,000 /µL", reference_range="150,000 - 450,000 /µL", trend_status="Monitoring"),
            SerialLabTrend(parameter="Absolute Neutrophil Count (ANC)", baseline="4,100 /µL", interim="2,400 /µL", current="2,150 /µL", reference_range="1,500 - 7,000 /µL", trend_status="Favorable"),
            SerialLabTrend(parameter="Hemoglobin (Hb)", baseline="12.8 g/dL", interim="11.6 g/dL", current="11.4 g/dL", reference_range="13.0 - 17.0 g/dL", trend_status="Stable"),
            SerialLabTrend(parameter="Serum Creatinine", baseline="0.91 mg/dL", interim="0.92 mg/dL", current="0.94 mg/dL", reference_range="0.70 - 1.20 mg/dL", trend_status="Stable")
        ],
        stored_voice_memos=[
            ArchivedVoiceMemo(
                id="MEMO-HIST-01",
                encounter_date="16-Sep-2026",
                treating_oncologist="Dr. Arvind V. Kulkarni, MD, DM",
                audio_duration="0:32",
                transcript="Post-Cycle 2 checkup for Rajesh Sharma. Infusion completed without hypersensitivity. Mild cold-induced fingertip sensitivity noted. Ordered pre-Cycle 3 labs and reinforced cold avoidance protocol.",
                action_items_count=3
            ),
            ArchivedVoiceMemo(
                id="MEMO-HIST-02",
                encounter_date="02-Sep-2026",
                treating_oncologist="Dr. Arvind V. Kulkarni, MD, DM",
                audio_duration="0:28",
                transcript="Cycle 1 initiation consultation. Port-a-cath accessed cleanly. Prescribed supportive antiemetics and scheduled Cycle 2 for 16-Sep-2026.",
                action_items_count=2
            )
        ],
        key_historical_milestones=[
            {"date": "24-Jul-2026", "title": "Surgical Resection", "detail": "Laparoscopic Anterior Resection with R0 Clear Margins"},
            {"date": "14-Aug-2026", "title": "Post-Op Restaging CT", "detail": "CT Abdomen/Pelvis: Intact colorectal staple line, zero hepatic lesions"},
            {"date": "02-Sep-2026", "title": "Chemotherapy Initiation", "detail": "Adjuvant mFOLFOX-6 Cycle 1 administered"},
            {"date": "16-Sep-2026", "title": "Cycle 2 Delivered", "detail": "Tolerated well with full dose intensity"},
            {"date": "30-Sep-2026", "title": "Pre-Cycle 3 Evaluation", "detail": "Labs verified safe; CEA durably suppressed at 2.8 ng/mL"}
        ]
    ),
    "P002": PatientHistoryArchive(
        patient_id="P002",
        diagnosis_anchor_date="20-Jul-2026",
        primary_surgery_summary="Left Breast Lumpectomy & Sentinel Lymph Node Biopsy (02-Aug-2026). R0 clear margins (>2mm), 3 sentinel nodes isolated and confirmed negative (0/3).",
        total_chemo_cycles_delivered="1 of 4 Cycles Delivered (AC Phase)",
        radiation_summary="Planned Whole Breast Irradiation following completion of Paclitaxel",
        serial_lab_trends=[
            SerialLabTrend(parameter="Absolute Neutrophil Count (ANC)", baseline="3,600 /µL", interim="1,100 /µL", current="2,800 /µL", reference_range="1,500 - 7,000 /µL", trend_status="Favorable"),
            SerialLabTrend(parameter="Hemoglobin (Hb)", baseline="12.6 g/dL", interim="12.2 g/dL", current="12.1 g/dL", reference_range="12.0 - 15.5 g/dL", trend_status="Stable"),
            SerialLabTrend(parameter="Left Ventricular Ejection Fraction (LVEF)", baseline="63%", interim="63%", current="63%", reference_range="55% - 70%", trend_status="Favorable")
        ],
        stored_voice_memos=[
            ArchivedVoiceMemo(
                id="MEMO-HIST-B01",
                encounter_date="14-Sep-2026",
                treating_oncologist="Dr. Meenakshi Sundaram, MD",
                audio_duration="0:26",
                transcript="Cycle 1 dose-dense AC infused smoothly. Prescribed oral antiemetics and arranged pegfilgrastim 6mg on day 2. Advised scalp cooling education.",
                action_items_count=2
            )
        ],
        key_historical_milestones=[
            {"date": "02-Aug-2026", "title": "Breast Conserving Surgery", "detail": "Left lumpectomy and SLNB (0/3 negative nodes)"},
            {"date": "10-Aug-2026", "title": "Cardio-Oncology Baseline", "detail": "Echocardiogram confirms baseline LVEF 63% and normal GLS"},
            {"date": "14-Sep-2026", "title": "Cycle 1 AC Initiated", "detail": "Doxorubicin + Cyclophosphamide with G-CSF support"}
        ]
    ),
    "P003": PatientHistoryArchive(
        patient_id="P003",
        diagnosis_anchor_date="10-Jun-2026",
        primary_surgery_summary="Inoperable Stage IV NSCLC. CT-guided core biopsy confirmed Adenocarcinoma; NGS detected EGFR Exon 21 L858R mutation.",
        total_chemo_cycles_delivered="Targeted Therapy: Month 3 of 12 (Osimertinib 80mg Daily)",
        radiation_summary="None Required (Systemic Control Maintained)",
        serial_lab_trends=[
            SerialLabTrend(parameter="Target Lesion Size (CT Chest)", baseline="3.4 x 2.8 cm", interim="2.6 x 2.1 cm", current="1.8 x 1.4 cm", reference_range="Regression", trend_status="Favorable"),
            SerialLabTrend(parameter="SGPT (ALT)", baseline="22 U/L", interim="26 U/L", current="32 U/L", reference_range="7 - 45 U/L", trend_status="Stable"),
            SerialLabTrend(parameter="Serum Creatinine", baseline="0.88 mg/dL", interim="0.90 mg/dL", current="0.91 mg/dL", reference_range="0.70 - 1.20 mg/dL", trend_status="Stable")
        ],
        stored_voice_memos=[
            ArchivedVoiceMemo(
                id="MEMO-HIST-C01",
                encounter_date="28-Jun-2026",
                treating_oncologist="Dr. Arvind V. Kulkarni, MD, DM",
                audio_duration="0:34",
                transcript="Confirmed EGFR L858R mutation from molecular sequencing. Commenced first-line Osimertinib 80mg oral daily. Patient educated on rash and diarrhea management.",
                action_items_count=3
            )
        ],
        key_historical_milestones=[
            {"date": "28-Jun-2026", "title": "Targeted Therapy Start", "detail": "Osimertinib 80mg oral daily initiated"},
            {"date": "22-Sep-2026", "title": "3-Month Restaging CT", "detail": "47% tumor shrinkage (RECIST 1.1 Partial Response)"}
        ]
    ),
    "P004": PatientHistoryArchive(
        patient_id="P004",
        diagnosis_anchor_date="02-May-2026",
        primary_surgery_summary="Optimal Interval Debulking Surgery: Total Abdominal Hysterectomy, Bilateral Salpingo-Oophorectomy & Omentectomy (22-Jun-2026). R0 microscopic debulking.",
        total_chemo_cycles_delivered="3 of 6 Cycles Delivered (Adjuvant Carbo-Taxol + Bevacizumab)",
        radiation_summary="None (Systemic Adjuvant Protocol)",
        serial_lab_trends=[
            SerialLabTrend(parameter="Serum CA-125", baseline="480 U/mL", interim="68 U/mL", current="24.2 U/mL", reference_range="< 35.0 U/mL", trend_status="Favorable"),
            SerialLabTrend(parameter="Urine Protein / Creatinine", baseline="0.12", interim="0.15", current="0.18", reference_range="< 0.50", trend_status="Stable"),
            SerialLabTrend(parameter="Hemoglobin (Hb)", baseline="12.0 g/dL", interim="11.2 g/dL", current="10.8 g/dL", reference_range="12.0 - 15.5 g/dL", trend_status="Monitoring")
        ],
        stored_voice_memos=[
            ArchivedVoiceMemo(
                id="MEMO-HIST-D01",
                encounter_date="04-Sep-2026",
                treating_oncologist="Dr. Radhika Sen, MD, DNB",
                audio_duration="0:30",
                transcript="Cycle 3 Carbo-Taxol-Bevacizumab administered without event. Blood pressure normal at 122/78. CA-125 trending down nicely.",
                action_items_count=2
            )
        ],
        key_historical_milestones=[
            {"date": "22-Jun-2026", "title": "Optimal Cytoreduction", "detail": "Interval debulking surgery with complete macroscopic clearance"},
            {"date": "04-Sep-2026", "title": "Cycle 3 Completed", "detail": "Delivered with Bevacizumab 15mg/kg"},
            {"date": "26-Sep-2026", "title": "CA-125 Normalized", "detail": "Biochemical remission reached at 24.2 U/mL"}
        ]
    ),
    "P005": PatientHistoryArchive(
        patient_id="P005",
        diagnosis_anchor_date="15-May-2026",
        primary_surgery_summary="Bone Marrow Aspiration & Trephine Biopsy: 45% plasma cell infiltrate, IgG Kappa clonal restriction, standard risk cytogenetics.",
        total_chemo_cycles_delivered="3 of 4 Cycles Delivered (VRd Induction Protocol)",
        radiation_summary="None",
        serial_lab_trends=[
            SerialLabTrend(parameter="Serum M-Protein Spike", baseline="3.2 g/dL", interim="1.4 g/dL", current="0.4 g/dL", reference_range="Undetected", trend_status="Favorable"),
            SerialLabTrend(parameter="Serum Free Kappa Light Chain", baseline="340 mg/L", interim="85 mg/L", current="26.4 mg/L", reference_range="3.3 - 19.4 mg/L", trend_status="Favorable"),
            SerialLabTrend(parameter="Serum Calcium (Corrected)", baseline="9.6 mg/dL", interim="9.2 mg/dL", current="9.1 mg/dL", reference_range="8.5 - 10.2 mg/dL", trend_status="Stable")
        ],
        stored_voice_memos=[
            ArchivedVoiceMemo(
                id="MEMO-HIST-E01",
                encounter_date="03-Sep-2026",
                treating_oncologist="Dr. Arvind V. Kulkarni, MD, DM",
                audio_duration="0:29",
                transcript="Cycle 3 VRd completed. Excellent tolerability on subcutaneous bortezomib. M-spike down substantially.",
                action_items_count=2
            )
        ],
        key_historical_milestones=[
            {"date": "03-Sep-2026", "title": "Cycle 3 VRd Completed", "detail": "Bortezomib + Lenalidomide + Dexamethasone"},
            {"date": "25-Sep-2026", "title": "VGPR Documented", "detail": "Serum M-spike reduced by >85% (0.4 g/dL)"}
        ]
    )
}

DOCUMENTS_DATA: Dict[str, List[ClinicalDocument]] = {
    "P001": [
        ClinicalDocument(
            id="DOC-P001-01",
            patient_id="P001",
            title="Pre-Cycle 3 Complete Blood Count & Renal Panel",
            category="CBC Blood Panel",
            date="30-Sep-2026",
            facility="Celabs Diagnostics Pvt. Ltd.",
            accreditation="NABL Accredited Lab #MC-2091 | CAP #782190",
            specimen_id="SPEC-99214-HEM",
            summary="Pre-chemotherapy hematologic and metabolic assessment prior to cycle 3 FOLFOX-6 infusion.",
            clinical_notes="Patient reports mild cold-induced dysesthesia. Tolerated cycle 2 well without febrile neutropenia.",
            table_data=[
                ClinicalTableRow(parameter="Hemoglobin", value="11.4", unit="g/dL", reference_range="13.0 - 17.0", flag="Low", notes="Mild normocytic anemia, stable from baseline"),
                ClinicalTableRow(parameter="Total Leukocyte Count (TLC)", value="4,200", unit="/µL", reference_range="4,000 - 10,000", flag="Normal", notes="Adequate marrow reserve"),
                ClinicalTableRow(parameter="Absolute Neutrophil Count (ANC)", value="2,150", unit="/µL", reference_range="1,500 - 7,000", flag="Normal", notes="Above safe threshold (1,500) for Oxaliplatin"),
                ClinicalTableRow(parameter="Platelet Count", value="138,000", unit="/µL", reference_range="150,000 - 450,000", flag="Low", notes="Grade 1 thrombocytopenia; acceptable for infusion"),
                ClinicalTableRow(parameter="Serum Creatinine", value="0.94", unit="mg/dL", reference_range="0.70 - 1.20", flag="Normal", notes="Normal renal clearance"),
                ClinicalTableRow(parameter="eGFR (CKD-EPI)", value="88", unit="mL/min/1.73m²", reference_range="> 60", flag="Normal", notes="Full dose clearance supported"),
                ClinicalTableRow(parameter="Serum CEA (Carcinoembryonic Ag)", value="2.8", unit="ng/mL", reference_range="< 3.0 (Non-smoker)", flag="Normal", notes="Down from 6.4 pre-operative baseline")
            ],
            findings=[
                "Hemoglobin 11.4 g/dL, stable compared to cycle 2 (11.6 g/dL).",
                "Platelets at 138,000/µL, mild drop consistent with oxaliplatin myelosuppression, safe for cycle 3.",
                "ANC 2,150/µL meets clinical protocol requirements (>1,500/µL).",
                "CEA level normalized at 2.8 ng/mL confirming biochemical disease control."
            ],
            conclusion="Satisfactory hematologic reserve and normal renal parameters. Meets clinical criteria to proceed with planned cycle 3 mFOLFOX-6.",
            reporting_specialist="Dr. Sunita Rao, MD (Hematopathology), Celabs Diagnostics",
            source_file_name="Rajesh_Sharma_CBC_Renal_30Sep2026.pdf",
            file_size="412 KB",
            status="Processed & Verified"
        ),
        ClinicalDocument(
            id="DOC-P001-02",
            patient_id="P001",
            title="Post-Operative Baseline Contrast-Enhanced CT Abdomen & Pelvis",
            category="CT Abdomen Scan",
            date="14-Aug-2026",
            facility="Celabs Diagnostics Pvt. Ltd. (Advanced Imaging Wing)",
            accreditation="NABL & AERB Certified Radiology Suite",
            specimen_id="RAD-CT-77402",
            summary="Baseline restaging CT abdomen/pelvis post laparoscopic anterior resection for sigmoid colon adenocarcinoma.",
            clinical_notes="Surgical staple line intact in lower pelvic retroperitoneum. No gross recurrent mass.",
            table_data=[
                ClinicalTableRow(parameter="Liver Parenchyma", value="Normal", unit="", reference_range="Homogeneous", flag="Normal", notes="No focal hypodense hepatic lesions or metastatic deposits"),
                ClinicalTableRow(parameter="Peritoneal Cavity", value="Clear", unit="", reference_range="No free fluid", flag="Normal", notes="No peritoneal nodularity or ascites"),
                ClinicalTableRow(parameter="Surgical Anastomosis", value="Intact", unit="", reference_range="Patent lumen", flag="Normal", notes="Concentric staple line without extrinsic mass effect"),
                ClinicalTableRow(parameter="Retroperitoneal Lymph Nodes", value="< 6 mm", unit="mm", reference_range="< 10 mm", flag="Normal", notes="Subcentimeter reactive nodes, no pathological lymphadenopathy")
            ],
            findings=[
                "Status post sigmoidectomy with intact colorectal anastomosis.",
                "No focal hepatic parenchymal lesions, cysts, or distant metastases.",
                "Spleen, pancreas, kidneys, and adrenal glands appear unremarkable.",
                "No pathologic retroperitoneal, mesenteric, or pelvic lymphadenopathy."
            ],
            conclusion="No evidence of local recurrence or distant metastatic disease. Baseline established prior to adjuvant mFOLFOX-6.",
            reporting_specialist="Dr. K. N. Venkatesh, MD (Radiodiagnosis), Celabs Diagnostics",
            source_file_name="Rajesh_Sharma_CT_Abdomen_Baseline_14Aug2026.pdf",
            file_size="1.8 MB",
            status="Processed & Verified"
        ),
        ClinicalDocument(
            id="DOC-P001-03",
            patient_id="P001",
            title="Surgical Histopathology Report: Sigmoidectomy Specimen",
            category="Histopathology Report",
            date="28-Jul-2026",
            facility="Apex Histopathology & Molecular Diagnostics",
            accreditation="College of American Pathologists (CAP) Accredited",
            specimen_id="HISTO-2026-6619",
            summary="Detailed surgical pathology review of resected sigmoid colon segment with regional lymphadenectomy.",
            clinical_notes="Clinical indication: Obstructing mass of sigmoid colon. Laparoscopic anterior resection.",
            table_data=[
                ClinicalTableRow(parameter="Histologic Subtype", value="Adenocarcinoma", unit="", reference_range="Moderate diff", flag="Normal", notes="G2 moderately differentiated glandular architecture"),
                ClinicalTableRow(parameter="Depth of Invasion", value="pT3", unit="", reference_range="Invades subserosa", flag="High", notes="Extends through muscularis propria into pericolic fat"),
                ClinicalTableRow(parameter="Lymph Nodes Harvested", value="21 nodes", unit="", reference_range=">= 12 recommended", flag="Normal", notes="Adequate oncologic lymph node sampling"),
                ClinicalTableRow(parameter="Positive Lymph Nodes", value="3 of 21", unit="", reference_range="0 nodes", flag="High", notes="Metastatic adenocarcinoma in 3 pericolic nodes (pN1b)"),
                ClinicalTableRow(parameter="Proximal & Distal Margins", value="Negative (> 5 cm)", unit="", reference_range="Negative", flag="Normal", notes="Free of malignancy"),
                ClinicalTableRow(parameter="Radial (Circumferential) Margin", value="Clear (8 mm)", unit="", reference_range="> 1 mm", flag="Normal", notes="Adequate radial clearance"),
                ClinicalTableRow(parameter="Mismatch Repair (MMR)", value="Proficient (MSS)", unit="", reference_range="Intact MLH1/MSH2/MSH6/PMS2", flag="Normal", notes="Intact nuclear expression of all 4 MMR proteins")
            ],
            findings=[
                "Ulcerated infiltrative adenocarcinoma of sigmoid colon measuring 4.2 x 3.0 cm.",
                "Invasion into pericolic soft tissues (pT3).",
                "3 out of 21 isolated lymph nodes contain metastatic tumor deposits (pN1b).",
                "Lymphovascular invasion identified; perineural invasion is absent.",
                "Immunohistochemistry: MLH1+, MSH2+, MSH6+, PMS2+ (Mismatch Repair Proficient / MSS)."
            ],
            conclusion="Pathologic Stage: pT3 N1b M0 (Stage IIIB, AJCC 8th Edition). Adjuvant systemic chemotherapy indicated.",
            reporting_specialist="Prof. Dr. Elizabeth George, MD, FRCPath",
            source_file_name="Rajesh_Sharma_Histopathology_Sigmoid_28Jul2026.pdf",
            file_size="680 KB",
            status="Processed & Verified"
        )
    ],
    "P002": [
        ClinicalDocument(
            id="DOC-P002-01",
            patient_id="P002",
            title="Pre-Cycle 2 Complete Blood Count & Electrolyte Profile",
            category="CBC Blood Panel",
            date="28-Sep-2026",
            facility="Celabs Diagnostics Pvt. Ltd.",
            accreditation="NABL & CAP Certified",
            specimen_id="SPEC-77318-HEM",
            summary="Routine surveillance labs prior to second infusion of Doxorubicin and Cyclophosphamide.",
            clinical_notes="Patient experienced mild nausea day 2-4 controlled with ondansetron. Mild alopecia initiated.",
            table_data=[
                ClinicalTableRow(parameter="Hemoglobin", value="12.1", unit="g/dL", reference_range="12.0 - 15.5", flag="Normal", notes="Within normal limits"),
                ClinicalTableRow(parameter="TLC", value="5,100", unit="/µL", reference_range="4,000 - 10,000", flag="Normal", notes="Recovered after post-chemo nadir"),
                ClinicalTableRow(parameter="Absolute Neutrophil Count", value="2,800", unit="/µL", reference_range="1,500 - 7,000", flag="Normal", notes="PEG-GCSF administered on day 2 supported recovery"),
                ClinicalTableRow(parameter="Platelet Count", value="195,000", unit="/µL", reference_range="150,000 - 450,000", flag="Normal", notes="Normal clotting reserve"),
                ClinicalTableRow(parameter="Total Bilirubin", value="0.7", unit="mg/dL", reference_range="0.2 - 1.2", flag="Normal", notes="Safe for anthracycline metabolism"),
                ClinicalTableRow(parameter="SGPT (ALT)", value="28", unit="U/L", reference_range="7 - 35", flag="Normal", notes="Normal hepatic transaminases")
            ],
            findings=[
                "Hemoglobin preserved at 12.1 g/dL.",
                "ANC 2,800/µL reflects robust marrow response following G-CSF support.",
                "Hepatic and renal panels strictly within normal limits."
            ],
            conclusion="Adequate marrow and organ reserve. Proceed with planned Cycle 2 AC.",
            reporting_specialist="Dr. Sunita Rao, MD, Celabs Diagnostics",
            source_file_name="Anita_Devi_CBC_28Sep2026.pdf",
            file_size="380 KB",
            status="Processed & Verified"
        ),
        ClinicalDocument(
            id="DOC-P002-02",
            patient_id="P002",
            title="Transthoracic Echocardiogram (Baseline Cardio-Oncology)",
            category="Echo LVEF",
            date="10-Aug-2026",
            facility="Apex Heart & Vascular Care Centre",
            accreditation="NABH Accredited Cardiology Wing",
            specimen_id="ECHO-2026-902",
            summary="Cardiovascular risk screening prior to initiating anthracycline-based chemotherapy.",
            clinical_notes="No history of hypertension or ischemic heart disease.",
            table_data=[
                ClinicalTableRow(parameter="Left Ventricular Ejection Fraction (LVEF)", value="63%", unit="%", reference_range="55% - 70%", flag="Normal", notes="Normal global LV systolic function"),
                ClinicalTableRow(parameter="Global Longitudinal Strain (GLS)", value="-20.4%", unit="%", reference_range="< -18.0%", flag="Normal", notes="No subclinical myocardial dysfunction"),
                ClinicalTableRow(parameter="Diastolic Function", value="Grade I (Mild relaxation abnormality)", unit="", reference_range="Normal", flag="Normal", notes="Age-appropriate finding")
            ],
            findings=[
                "Normal LV chamber dimensions with wall motion score 1.0 (no regional abnormalities).",
                "Calculated Simpson's biplane LVEF is 63%.",
                "Baseline GLS -20.4% confirms preservation of myocardial strain."
            ],
            conclusion="Cardiac function fully preserved. Low cardiotoxicity risk for doxorubicin regimen.",
            reporting_specialist="Dr. Harshavardhan Joshi, MD, DM (Cardiology)",
            source_file_name="Anita_Devi_Echo_Cardio_10Aug2026.pdf",
            file_size="520 KB",
            status="Processed & Verified"
        )
    ],
    "P003": [
        ClinicalDocument(
            id="DOC-P003-01",
            patient_id="P003",
            title="High-Resolution Restaging CT Chest with IV Contrast",
            category="CT Abdomen Scan",
            date="22-Sep-2026",
            facility="Celabs Diagnostics Pvt. Ltd.",
            accreditation="NABL & AERB Certified",
            specimen_id="RAD-CT-89104",
            summary="Three-month response assessment CT chest while on targeted Osimertinib therapy.",
            clinical_notes="Patient notes marked improvement in dry cough and exercise tolerance. Mild acneiform rash on cheeks.",
            table_data=[
                ClinicalTableRow(parameter="Right Upper Lobe Index Lesion", value="1.8 x 1.4 cm", unit="cm", reference_range="Baseline 3.4 x 2.8 cm", flag="Normal", notes="Significant dimensional regression (-47% by RECIST 1.1)"),
                ClinicalTableRow(parameter="Subcarinal Lymph Node", value="8 mm", unit="mm", reference_range="Baseline 16 mm", flag="Normal", notes="Decreased in short axis from 16 mm to 8 mm"),
                ClinicalTableRow(parameter="Contralateral Left Lung Nodules", value="Stable / Regressed", unit="", reference_range="Non-calcified", flag="Normal", notes="Two 4 mm nodules stable, third resolved"),
                ClinicalTableRow(parameter="Pleural Cavity", value="No effusion", unit="", reference_range="Clear", flag="Normal", notes="Previous trace right pleural effusion resolved")
            ],
            findings=[
                "Right upper lobe primary tumor shows 47% reduction in unidimensional diameter (Partial Response).",
                "Mediastinal and hilar lymphadenopathy significantly downsized.",
                "Resolution of previous right trace pleural effusion.",
                "No new pulmonary, osseous, or upper abdominal lesions."
            ],
            conclusion="Partial Response (PR) by RECIST 1.1 criteria to first-line Osimertinib. Excellent clinical & radiological response.",
            reporting_specialist="Dr. K. N. Venkatesh, MD (Radiodiagnosis), Celabs Diagnostics",
            source_file_name="Vikram_Singh_CT_Chest_22Sep2026.pdf",
            file_size="2.1 MB",
            status="Processed & Verified"
        )
    ],
    "P004": [
        ClinicalDocument(
            id="DOC-P004-01",
            patient_id="P004",
            title="Pre-Cycle 4 Serum Tumor Marker & Metabolic Profile",
            category="CBC Blood Panel",
            date="26-Sep-2026",
            facility="Celabs Diagnostics Pvt. Ltd.",
            accreditation="NABL & CAP Certified",
            specimen_id="SPEC-44109-ONC",
            summary="Interim biochemical evaluation of CA-125 and hematologic parameters prior to cycle 4 adjuvant chemo.",
            clinical_notes="Asymptomatic, ECOG performance status 1. Blood pressure normal under bevacizumab monitoring.",
            table_data=[
                ClinicalTableRow(parameter="Serum CA-125", value="24.2", unit="U/mL", reference_range="< 35.0", flag="Normal", notes="Normalized (down from 480 pre-op and 68 post-cycle 2)"),
                ClinicalTableRow(parameter="Hemoglobin", value="10.8", unit="g/dL", reference_range="12.0 - 15.5", flag="Low", notes="Grade 1 anemia, stable"),
                ClinicalTableRow(parameter="Platelet Count", value="214,000", unit="/µL", reference_range="150,000 - 450,000", flag="Normal", notes="Normal"),
                ClinicalTableRow(parameter="Urinary Protein : Creatinine", value="0.18", unit="ratio", reference_range="< 0.50", flag="Normal", notes="No significant proteinuria; safe for Bevacizumab")
            ],
            findings=[
                "CA-125 level has successfully normalized to 24.2 U/mL (below reference threshold of 35 U/mL).",
                "Renal profile and urine protein/creatinine ratio confirm no bevacizumab-induced nephrotoxicity.",
                "Liver transaminases and electrolytes within normal expected range."
            ],
            conclusion="Biochemical remission maintained. Safe to administer Cycle 4 Carboplatin/Paclitaxel/Bevacizumab.",
            reporting_specialist="Dr. Sunita Rao, MD, Celabs Diagnostics",
            source_file_name="Priya_Nair_CA125_CBC_26Sep2026.pdf",
            file_size="420 KB",
            status="Processed & Verified"
        )
    ],
    "P005": [
        ClinicalDocument(
            id="DOC-P005-01",
            patient_id="P005",
            title="Cycle 4 Serum Protein Electrophoresis & Light Chains",
            category="CBC Blood Panel",
            date="25-Sep-2026",
            facility="Celabs Diagnostics Pvt. Ltd.",
            accreditation="NABL & CAP Certified",
            specimen_id="SPEC-12093-MYEL",
            summary="Monoclonal protein quantification and free light chain monitoring for IgG kappa multiple myeloma.",
            clinical_notes="No bone pain. No symptomatic peripheral neuropathy on subcutaneous bortezomib.",
            table_data=[
                ClinicalTableRow(parameter="Serum M-Protein Spike (SPEP)", value="0.4", unit="g/dL", reference_range="Not detected", flag="High", notes="Marked reduction from 3.2 g/dL at baseline"),
                ClinicalTableRow(parameter="Serum Free Kappa Light Chain", value="26.4", unit="mg/L", reference_range="3.3 - 19.4", flag="High", notes="Markedly down from 340 mg/L"),
                ClinicalTableRow(parameter="Serum Free Lambda Light Chain", value="14.8", unit="mg/L", reference_range="5.7 - 26.3", flag="Normal", notes="Normal range"),
                ClinicalTableRow(parameter="Kappa / Lambda Ratio", value="1.78", unit="", reference_range="0.26 - 1.65", flag="High", notes="Approaching normalization (baseline 28.4)"),
                ClinicalTableRow(parameter="Serum Calcium (Corrected)", value="9.1", unit="mg/dL", reference_range="8.5 - 10.2", flag="Normal", notes="Eucalcemic, no hypercalcemia"),
                ClinicalTableRow(parameter="Serum Creatinine", value="1.05", unit="mg/dL", reference_range="0.70 - 1.20", flag="Normal", notes="Stable renal function")
            ],
            findings=[
                "Serum M-spike reduced from 3.2 g/dL to 0.4 g/dL (> 85% reduction, fulfilling Very Good Partial Response criteria).",
                "Involved free light chain significantly reduced.",
                "Renal function and calcium levels remain stable with no CRAB criteria activation."
            ],
            conclusion="Very Good Partial Response (VGPR) achieved on VRd. Proceed with cycle 4 and evaluate autologous stem cell transplant timing.",
            reporting_specialist="Dr. Sunita Rao, MD, Celabs Diagnostics",
            source_file_name="Mohammed_AlFarsi_SPEP_25Sep2026.pdf",
            file_size="530 KB",
            status="Processed & Verified"
        )
    ]
}

TIMELINE_DATA: Dict[str, List[TimelineEvent]] = {
    "P001": [
        TimelineEvent(
            id="EVT-01",
            patient_id="P001",
            date="30-Sep-2026",
            event_type="Visit",
            title="Pre-Chemo Outpatient Review & Lab Verification",
            subtitle="Outpatient Oncology Clinic • Room 402",
            description="Clinical evaluation prior to Cycle 3 mFOLFOX-6. Peripheral neuropathy assessed: Grade 1 cold-induced dysesthesia of fingertips, non-limiting. Blood panel verified.",
            badge="Verified Safe for Infusion",
            metrics={"ANC": "2,150/µL", "Platelets": "138,000/µL", "CEA": "2.8 ng/mL", "Toxicity": "Grade 1 Neuro"},
            status="Completed"
        ),
        TimelineEvent(
            id="EVT-02",
            patient_id="P001",
            date="16-Sep-2026",
            event_type="Chemo",
            title="Adjuvant mFOLFOX-6 • Cycle 2 Infusion",
            subtitle="Day-Care Oncology Infusion Suite",
            description="Oxaliplatin 85mg/m² IV, Leucovorin 400mg/m², 5-FU bolus 400mg/m² followed by 46-hr continuous ambulatory elastomeric pump (2,400mg/m²). Completed without infusion reactions.",
            badge="Cycle 2 Completed",
            metrics={"Dose Delivered": "100%", "Pre-meds": "Dexamethasone + Palonosetron", "Tolerability": "Good"},
            status="Completed"
        ),
        TimelineEvent(
            id="EVT-03",
            patient_id="P001",
            date="02-Sep-2026",
            event_type="Chemo",
            title="Adjuvant mFOLFOX-6 • Cycle 1 (Initiation)",
            subtitle="Day-Care Oncology Infusion Suite",
            description="First adjuvant cycle commenced 5 weeks post laparoscopic sigmoid resection. Port-a-cath accessed cleanly. Patient educated on avoiding cold liquids and touching cold surfaces.",
            badge="Cycle 1 Completed",
            metrics={"Port Status": "Patent, Aspirates blood", "Education": "Neurotoxicity sheet provided"},
            status="Completed"
        ),
        TimelineEvent(
            id="EVT-04",
            patient_id="P001",
            date="14-Aug-2026",
            event_type="Scans",
            title="Post-Operative Baseline Contrast-Enhanced CT Abdomen",
            subtitle="Celabs Diagnostics Advanced Radiology",
            description="CT Abdomen & Pelvis confirmed intact surgical staple line with no residual or metastatic lesions. Hepatic parenchyma clear. Zero ascites.",
            badge="No Metastatic Disease",
            metrics={"Liver Mets": "0 / Clear", "Anastomosis": "Intact", "Peritoneum": "Clear"},
            status="Completed"
        ),
        TimelineEvent(
            id="EVT-05",
            patient_id="P001",
            date="24-Jul-2026",
            event_type="Surgery",
            title="Laparoscopic Anterior Resection of Sigmoid Colon",
            subtitle="Main Surgical Theatre • Team Lead: Dr. R. K. Saxena",
            description="Laparoscopic resection of obstructing sigmoid tumor with high ligation of inferior mesenteric vessels and total mesorectal excision. Colorectal end-to-end EEA stapled anastomosis.",
            badge="R0 Curative Resection",
            metrics={"Blood Loss": "120 mL", "Margins": "Negative (>5cm)", "Nodes": "21 harvested (3 positive)"},
            status="Completed"
        )
    ],
    "P002": [
        TimelineEvent(
            id="EVT-B01",
            patient_id="P002",
            date="28-Sep-2026",
            event_type="Visit",
            title="Cycle 2 Pre-Treatment Toxicity Assessment",
            subtitle="Breast Oncology Day Care",
            description="Patient examined post Cycle 1 AC. Well tolerated. No oral mucositis. Mild alopecia noted. LVEF baseline confirmed at 63%.",
            badge="Ready for Cycle 2",
            metrics={"LVEF": "63%", "ANC": "2,800/µL", "Nausea": "Grade 1 (Controlled)"},
            status="Completed"
        ),
        TimelineEvent(
            id="EVT-B02",
            patient_id="P002",
            date="14-Sep-2026",
            event_type="Chemo",
            title="Adjuvant Dose-Dense AC • Cycle 1",
            subtitle="Day Care Infusion",
            description="Doxorubicin 60mg/m² + Cyclophosphamide 600mg/m² IV administered. Pegfilgrastim 6mg SubQ given 24 hours later.",
            badge="Cycle 1 Completed",
            metrics={"Dose": "100%", "G-CSF": "Pegfilgrastim Administered"},
            status="Completed"
        ),
        TimelineEvent(
            id="EVT-B03",
            patient_id="P002",
            date="02-Aug-2026",
            event_type="Surgery",
            title="Left Breast Lumpectomy & Sentinel Lymph Node Biopsy",
            subtitle="Apex Surgical Oncology",
            description="Wide local excision with negative margins. 3 sentinel nodes identified via dual tracer (radiocolloid + blue dye); all 3 negative for metastatic carcinoma.",
            badge="Clear Margins (R0)",
            metrics={"Tumor Size": "2.2 cm", "Margins": "> 2 mm", "SLN Status": "0 / 3 Negative"},
            status="Completed"
        )
    ],
    "P003": [
        TimelineEvent(
            id="EVT-C01",
            patient_id="P003",
            date="22-Sep-2026",
            event_type="Scans",
            title="3-Month Restaging CT Chest & Upper Abdomen",
            subtitle="Celabs Diagnostics Radiology",
            description="High-resolution CT demonstrated 47% reduction in primary right upper lobe tumor mass (RECIST 1.1 Partial Response). Mediastinal lymph nodes normalized.",
            badge="Partial Response (RECIST -47%)",
            metrics={"Primary Mass": "1.8 x 1.4 cm (from 3.4)", "Lymph Nodes": "Subcentimeter", "Pleural Fluid": "Resolved"},
            status="Completed"
        ),
        TimelineEvent(
            id="EVT-C02",
            patient_id="P003",
            date="28-Jun-2026",
            event_type="Chemo",
            title="Initiation of First-Line Osimertinib 80mg Oral Daily",
            subtitle="Thoracic Oncology Clinic",
            description="Following confirmation of EGFR Exon 21 L858R mutation via next-generation sequencing, third-generation EGFR TKI Osimertinib initiated at 80mg once daily.",
            badge="Targeted Therapy Active",
            metrics={"Regimen": "Osimertinib 80mg PO QD", "EGFR Variant": "L858R Mutation Detected"},
            status="Completed"
        )
    ],
    "P004": [
        TimelineEvent(
            id="EVT-D01",
            patient_id="P004",
            date="26-Sep-2026",
            event_type="Visit",
            title="Pre-Cycle 4 Biochemical Assessment & CA-125 Review",
            subtitle="Gynecologic Oncology Outpatient",
            description="CA-125 tumor marker verified at 24.2 U/mL (normalized). Urine protein negative. Normal baseline blood pressure.",
            badge="CA-125 Normalized (<35)",
            metrics={"CA-125": "24.2 U/mL", "BP": "122/78 mmHg", "Proteinuria": "Negative (0.18 ratio)"},
            status="Completed"
        ),
        TimelineEvent(
            id="EVT-D02",
            patient_id="P004",
            date="04-Sep-2026",
            event_type="Chemo",
            title="Adjuvant Carboplatin + Paclitaxel + Bevacizumab • Cycle 3",
            subtitle="Day Care Infusion",
            description="Carboplatin AUC 5, Paclitaxel 175mg/m², Bevacizumab 15mg/kg infused over 4 hours. No hypersensitivity.",
            badge="Cycle 3 Completed",
            metrics={"Bevacizumab": "15 mg/kg Delivered", "Pre-meds": "H1/H2 blockers + Dexamethasone"},
            status="Completed"
        )
    ],
    "P005": [
        TimelineEvent(
            id="EVT-E01",
            patient_id="P005",
            date="25-Sep-2026",
            event_type="Visit",
            title="Cycle 4 Response Evaluation & SPEP Review",
            subtitle="Hematology-Oncology Clinic",
            description="Serum protein electrophoresis confirms serum M-spike dropped to 0.4 g/dL from 3.2 g/dL (>85% reduction, Very Good Partial Response).",
            badge="VGPR Achieved",
            metrics={"M-Spike": "0.4 g/dL (from 3.2)", "Kappa/Lambda": "1.78", "Creatinine": "1.05 mg/dL"},
            status="Completed"
        ),
        TimelineEvent(
            id="EVT-E02",
            patient_id="P005",
            date="03-Sep-2026",
            event_type="Chemo",
            title="VRd Induction Regimen • Cycle 3 Completed",
            subtitle="Outpatient Hematology",
            description="Bortezomib 1.3mg/m² SubQ, Lenalidomide 25mg PO Days 1-14, Dexamethasone 20mg Days 1,2,8,9,15,16. Aspirin 81mg thromboprophylaxis maintained.",
            badge="Cycle 3 Completed",
            metrics={"Thromboprophylaxis": "Aspirin Active", "Neuropathy": "Grade 0 / None"},
            status="Completed"
        )
    ]
}

DELTA_SUMMARIES: Dict[str, DeltaSummary] = {
    "P001": DeltaSummary(
        patient_id="P001",
        headline="Key Operational Deltas Since Last Consult (Cycle 2 vs Cycle 3)",
        points=[
            "Hematology & Platelets: Platelet count shows anticipated mild chemotherapy-induced decline from 162,000/µL to 138,000/µL (Grade 1), safely above the 100,000/µL threshold required for oxaliplatin infusion.",
            "Biochemical Tumor Marker: Serum CEA remains durably suppressed at 2.8 ng/mL (down from pre-operative baseline of 6.4 ng/mL), demonstrating continued biochemical response.",
            "Toxicity & Symptom Profile: Emergence of mild cold-triggered fingertip dysesthesia (Grade 1 oxaliplatin sensory neuropathy); patient advised to adhere strictly to cold avoidance protocols."
        ],
        last_compared_date="30-Sep-2026",
        impact_level="Stable & Ready for Infusion"
    ),
    "P002": DeltaSummary(
        patient_id="P002",
        headline="Key Operational Deltas Since Last Consult (Cycle 1 vs Cycle 2)",
        points=[
            "Bone Marrow Recovery: ANC rebounded to 2,800/µL following prophylactic pegfilgrastim, with hemoglobin stable at 12.1 g/dL.",
            "Cardiovascular Baseline: Transthoracic echocardiogram confirms normal baseline LVEF of 63% with preserved global longitudinal strain (-20.4%).",
            "Symptom Control: Nausea remained well controlled (Grade 1) with oral antiemetics; scalp cooling education reviewed as mild alopecia commences."
        ],
        last_compared_date="28-Sep-2026",
        impact_level="Stable"
    ),
    "P003": DeltaSummary(
        patient_id="P003",
        headline="Key Operational Deltas: 3-Month Restaging vs Baseline",
        points=[
            "Radiological Response: 47% dimensional reduction of the right upper lobe target mass with resolution of pleural fluid (RECIST 1.1 Partial Response).",
            "Functional Capacity: Cough and dyspnea markedly improved; patient reports climbing 2 flights of stairs without supplemental oxygen.",
            "Toxicity Delta: Mild facial papulopustular rash noted (Grade 1 EGFR skin toxicity); topicals initiated with no dose interruption required."
        ],
        last_compared_date="22-Sep-2026",
        impact_level="Favorable Response"
    ),
    "P004": DeltaSummary(
        patient_id="P004",
        headline="Key Operational Deltas Since Cycle 3",
        points=[
            "Tumor Marker Normalization: CA-125 achieved complete biochemical normalization at 24.2 U/mL (down from 68 U/mL post-cycle 2 and 480 U/mL at presentation).",
            "Renal & Vascular Safety: Spot urine protein-to-creatinine ratio (0.18) and normotensive readings verify safety of continuing Bevacizumab.",
            "Hematology: Mild Grade 1 anemia (Hb 10.8 g/dL) is clinically stable and asymptomatic."
        ],
        last_compared_date="26-Sep-2026",
        impact_level="Favorable Response"
    ),
    "P005": DeltaSummary(
        patient_id="P005",
        headline="Key Operational Deltas: Cycle 4 vs Cycle 1 Baseline",
        points=[
            "Paraprotein Burden: Serum M-spike dropped by >85% (from 3.2 g/dL to 0.4 g/dL), fulfilling formal criteria for Very Good Partial Response (VGPR).",
            "Renal & Mineral Stability: Creatinine preserved at 1.05 mg/dL; serum calcium normal at 9.1 mg/dL with zero hypercalcemic symptoms.",
            "Treatment Tolerability: Absence of neurotoxicity on subcutaneous bortezomib; thromboprophylaxis compliance confirmed."
        ],
        last_compared_date="25-Sep-2026",
        impact_level="Favorable Response"
    )
}

ADMIN_TASKS: Dict[str, List[AdministrativeTask]] = {
    "P001": [
        AdministrativeTask(
            id="TSK-01",
            patient_id="P001",
            title="Authorize Day-Care Infusion for Cycle 3 mFOLFOX-6 (Oxaliplatin 85mg/m² + 5-FU 46hr pump)",
            category="Prescription",
            completed=True,
            priority="High",
            due_info="Immediate"
        ),
        AdministrativeTask(
            id="TSK-02",
            patient_id="P001",
            title="Order Pre-Cycle 4 Laboratory Panel (CBC with Differential, LFTs, Serum Creatinine)",
            category="Laboratory",
            completed=False,
            priority="High",
            due_info="Due in 12 days (prior to Cycle 4)"
        ),
        AdministrativeTask(
            id="TSK-03",
            patient_id="P001",
            title="Provide Peripheral Neuropathy Cold-Avoidance Patient Education Pamphlet",
            category="Administrative",
            completed=True,
            priority="Standard",
            due_info="Completed during visit"
        ),
        AdministrativeTask(
            id="TSK-04",
            patient_id="P001",
            title="Schedule Routine Clinical Nutrition Follow-up for Weight Maintenance",
            category="Referral",
            completed=False,
            priority="Routine",
            due_info="Within 2 weeks"
        )
    ],
    "P002": [
        AdministrativeTask(
            id="TSK-B01",
            patient_id="P002",
            title="Order Cycle 2 Doxorubicin + Cyclophosphamide infusion with Day 2 Pegfilgrastim",
            category="Prescription",
            completed=True,
            priority="High",
            due_info="Today"
        ),
        AdministrativeTask(
            id="TSK-B02",
            patient_id="P002",
            title="Schedule Follow-up Echocardiogram post-Cycle 4 prior to Paclitaxel initiation",
            category="Imaging",
            completed=False,
            priority="Standard",
            due_info="Due in 6 weeks"
        ),
        AdministrativeTask(
            id="TSK-B03",
            patient_id="P002",
            title="Refill supportive medications (Ondansetron 8mg PO, Dexamethasone 4mg PO)",
            category="Prescription",
            completed=False,
            priority="Standard",
            due_info="Today"
        )
    ],
    "P003": [
        AdministrativeTask(
            id="TSK-C01",
            patient_id="P003",
            title="Renew 90-day dispensing authorization for Osimertinib 80mg Oral Tablets",
            category="Prescription",
            completed=True,
            priority="High",
            due_info="Dispensed today"
        ),
        AdministrativeTask(
            id="TSK-C02",
            patient_id="P003",
            title="Schedule next restaging CT Chest & Brain MRI for month 6 surveillance",
            category="Imaging",
            completed=False,
            priority="Standard",
            due_info="Scheduled for Dec-2026"
        ),
        AdministrativeTask(
            id="TSK-C03",
            patient_id="P003",
            title="Prescribe topical Clindamycin 1% gel for Grade 1 facial rash",
            category="Prescription",
            completed=False,
            priority="Routine",
            due_info="Within 24 hours"
        )
    ],
    "P004": [
        AdministrativeTask(
            id="TSK-D01",
            patient_id="P004",
            title="Authorize Day-Care Infusion for Cycle 4 Carbo-Taxol + Bevacizumab",
            category="Prescription",
            completed=True,
            priority="High",
            due_info="Immediate"
        ),
        AdministrativeTask(
            id="TSK-D02",
            patient_id="P004",
            title="Order post-Cycle 4 Urine Protein/Creatinine and CBC monitoring",
            category="Laboratory",
            completed=False,
            priority="High",
            due_info="In 14 days"
        ),
        AdministrativeTask(
            id="TSK-D03",
            patient_id="P004",
            title="Refer to Clinical Genetics for formal post-test counseling regarding somatic status",
            category="Referral",
            completed=False,
            priority="Routine",
            due_info="Next month"
        )
    ],
    "P005": [
        AdministrativeTask(
            id="TSK-E01",
            patient_id="P005",
            title="Authorize Cycle 4 VRd regimen (Bortezomib SubQ + Lenalidomide 25mg)",
            category="Prescription",
            completed=True,
            priority="High",
            due_info="Today"
        ),
        AdministrativeTask(
            id="TSK-E02",
            patient_id="P005",
            title="Coordinate Blood and Marrow Transplant (BMT) consultation for autologous stem cell harvest",
            category="Referral",
            completed=False,
            priority="High",
            due_info="Within 10 days"
        ),
        AdministrativeTask(
            id="TSK-E03",
            patient_id="P005",
            title="Repeat Serum Free Light Chains and 24-hour urine protein after Cycle 4 completion",
            category="Laboratory",
            completed=False,
            priority="Standard",
            due_info="In 21 days"
        )
    ]
}

AUDIT_LOGS: Dict[str, List[AuditLogEntry]] = {
    "P001": [
        AuditLogEntry(
            id="AUD-01",
            patient_id="P001",
            timestamp="30-Sep-2026 10:14 AM",
            agent_action="AI agent successfully normalized and structured laboratory parameters from uploaded pre-chemotherapy blood report.",
            source_document="Rajesh_Sharma_CBC_Renal_30Sep2026.pdf",
            parameters_extracted=["Hemoglobin (11.4 g/dL)", "ANC (2,150/µL)", "Platelets (138,000/µL)", "Serum CEA (2.8 ng/mL)"],
            confidence_metric="High (Human Review Ready)",
            status="Verified",
            traceability_details={
                "source_facility": "Celabs Diagnostics Pvt. Ltd.",
                "verification_scope": "Automated range checks & oncologic toxicity grade mapping against CTCAE v5.0",
                "clinician_signoff": "Dr. Arvind V. Kulkarni (Signed off 30-Sep-2026 10:22 AM)",
                "audit_classification": "Laboratory Parameter Ingestion"
            }
        ),
        AuditLogEntry(
            id="AUD-02",
            patient_id="P001",
            timestamp="30-Sep-2026 10:15 AM",
            agent_action="Computed longitudinal operational delta comparing Cycle 2 and Cycle 3 laboratory values and toxicity status.",
            source_document="Multi-document Synthesis (Cycle 2 vs Cycle 3 Record)",
            parameters_extracted=["Platelet Delta (-24,000/µL)", "CEA Stability (2.8 ng/mL)", "Symptom Onset (Dysesthesia)"],
            confidence_metric="High (Human Review Ready)",
            status="Verified",
            traceability_details={
                "source_facility": "Apex Oncology Institute & Research Centre",
                "verification_scope": "Delta calculation engine cross-referencing previous electronic flowsheets",
                "clinician_signoff": "Dr. Arvind V. Kulkarni (Signed off 30-Sep-2026 10:24 AM)",
                "audit_classification": "Longitudinal Synthesis"
            }
        ),
        AuditLogEntry(
            id="AUD-03",
            patient_id="P001",
            timestamp="14-Aug-2026 03:45 PM",
            agent_action="Extracted radiological findings and anatomical measurements from post-operative contrast-enhanced CT scan.",
            source_document="Rajesh_Sharma_CT_Abdomen_Baseline_14Aug2026.pdf",
            parameters_extracted=["Anastomosis integrity", "Absence of hepatic lesions", "Lymph node dimensions (<6mm)"],
            confidence_metric="High (Human Review Ready)",
            status="Verified",
            traceability_details={
                "source_facility": "Celabs Diagnostics Advanced Radiology",
                "verification_scope": "Anatomic organ parser and RECIST non-target status verification",
                "clinician_signoff": "Dr. Arvind V. Kulkarni (Verified)",
                "audit_classification": "Imaging Ingestion"
            }
        ),
        AuditLogEntry(
            id="AUD-04",
            patient_id="P001",
            timestamp="28-Jul-2026 11:20 AM",
            agent_action="Parsed surgical histopathology report, cataloging pathological staging criteria and lymph node ratios.",
            source_document="Rajesh_Sharma_Histopathology_Sigmoid_28Jul2026.pdf",
            parameters_extracted=["pT3 Depth", "pN1b (3/21 nodes positive)", "MSS / MMR Proficient Status", "R0 Margins"],
            confidence_metric="High (Human Review Ready)",
            status="Verified",
            traceability_details={
                "source_facility": "Apex Histopathology & Molecular Diagnostics",
                "verification_scope": "TNM staging extractor and molecular marker profiler",
                "clinician_signoff": "Dr. Arvind V. Kulkarni (Verified)",
                "audit_classification": "Histopathology Ingestion"
            }
        )
    ],
    "P002": [
        AuditLogEntry(
            id="AUD-B01",
            patient_id="P002",
            timestamp="28-Sep-2026 09:30 AM",
            agent_action="AI agent normalized complete blood count and flagged adequate absolute neutrophil count after G-CSF.",
            source_document="Anita_Devi_CBC_28Sep2026.pdf",
            parameters_extracted=["ANC (2,800/µL)", "Hemoglobin (12.1 g/dL)", "SGPT (28 U/L)"],
            confidence_metric="High (Human Review Ready)",
            status="Verified",
            traceability_details={
                "source_facility": "Celabs Diagnostics Pvt. Ltd.",
                "verification_scope": "Hematologic threshold validation for Anthracycline dosing",
                "clinician_signoff": "Dr. Meenakshi Sundaram (Verified)",
                "audit_classification": "Laboratory Parameter Ingestion"
            }
        )
    ],
    "P003": [
        AuditLogEntry(
            id="AUD-C01",
            patient_id="P003",
            timestamp="22-Sep-2026 02:15 PM",
            agent_action="Extracted RECIST 1.1 unidimensional response metrics from 3-month restaging chest CT scan.",
            source_document="Vikram_Singh_CT_Chest_22Sep2026.pdf",
            parameters_extracted=["Target lesion dimensional change (-47%)", "Subcarinal node reduction", "Resolution of pleural fluid"],
            confidence_metric="High (Human Review Ready)",
            status="Verified",
            traceability_details={
                "source_facility": "Celabs Diagnostics Advanced Radiology",
                "verification_scope": "RECIST 1.1 criteria calculator comparing baseline and restaging imaging",
                "clinician_signoff": "Dr. Arvind V. Kulkarni (Verified)",
                "audit_classification": "Imaging Ingestion"
            }
        )
    ],
    "P004": [
        AuditLogEntry(
            id="AUD-D01",
            patient_id="P004",
            timestamp="26-Sep-2026 11:05 AM",
            agent_action="Extracted longitudinal CA-125 trend confirming progression below 35 U/mL threshold.",
            source_document="Priya_Nair_CA125_CBC_26Sep2026.pdf",
            parameters_extracted=["CA-125 (24.2 U/mL)", "Urine Protein/Creatinine (0.18)", "Platelets (214,000/µL)"],
            confidence_metric="High (Human Review Ready)",
            status="Verified",
            traceability_details={
                "source_facility": "Celabs Diagnostics Pvt. Ltd.",
                "verification_scope": "Biochemical marker trend verification and renal safety screening",
                "clinician_signoff": "Dr. Radhika Sen (Verified)",
                "audit_classification": "Laboratory Parameter Ingestion"
            }
        )
    ],
    "P005": [
        AuditLogEntry(
            id="AUD-E01",
            patient_id="P005",
            timestamp="25-Sep-2026 10:45 AM",
            agent_action="Quantified monoclonal paraprotein reduction and mapped response against IMWG VGPR guidelines.",
            source_document="Mohammed_AlFarsi_SPEP_25Sep2026.pdf",
            parameters_extracted=["Serum M-Spike (0.4 g/dL from 3.2)", "Kappa/Lambda ratio (1.78)", "Serum Calcium (9.1 mg/dL)"],
            confidence_metric="High (Human Review Ready)",
            status="Verified",
            traceability_details={
                "source_facility": "Celabs Diagnostics Pvt. Ltd.",
                "verification_scope": "IMWG Response Criteria mapping engine",
                "clinician_signoff": "Dr. Arvind V. Kulkarni (Verified)",
                "audit_classification": "Laboratory Parameter Ingestion"
            }
        )
    ]
}
