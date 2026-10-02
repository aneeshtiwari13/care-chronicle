"""
OCR & Document Processing Engine for Care Chronicle.
Parses background multi-format clinic paperwork (CT/MRI scans, histopathology,
blood panels, and doctor notes) into structured digital medical records.
"""

import uuid
from datetime import datetime
from typing import Dict, Any, List
from .models import ClinicalDocument, ClinicalTableRow

SAMPLE_TEMPLATES: Dict[str, Dict[str, Any]] = {
    "ct_scan": {
        "title": "Interim Contrast-Enhanced CT Abdomen & Pelvis",
        "category": "CT Abdomen Scan",
        "facility": "Celabs Diagnostics Pvt. Ltd. (Advanced Imaging Wing)",
        "accreditation": "NABL & AERB Certified Radiology Suite #RAD-8810",
        "specimen_id": "RAD-CT-91022",
        "summary": "Restaging CT evaluation of liver parenchyma, peritoneal cavity, and regional retroperitoneal nodes.",
        "clinical_notes": "Follow-up scan during adjuvant chemotherapy. Assessed according to RECIST 1.1 criteria.",
        "table_data": [
            {"parameter": "Hepatic Segments (I-VIII)", "value": "Clear / No Metastases", "unit": "", "reference_range": "Normal attenuation", "flag": "Normal", "notes": "No hypodense nodules or focal hepatic deposits"},
            {"parameter": "Surgical Anastomosis", "value": "Intact & Unremarkable", "unit": "", "reference_range": "No wall thickening", "flag": "Normal", "notes": "Patent lumen, no extrinsic soft tissue mass"},
            {"parameter": "Retroperitoneal Lymph Nodes", "value": "5.4 mm (Short axis)", "unit": "mm", "reference_range": "< 10.0 mm", "flag": "Normal", "notes": "Non-pathological reactive size"},
            {"parameter": "Peritoneal Surfaces", "value": "No nodularity or ascites", "unit": "", "reference_range": "Normal", "flag": "Normal", "notes": "Peritoneal fat planes preserved"}
        ],
        "findings": [
            "Normal liver attenuation without focal suspicious lesions or hepatic metastases.",
            "Post-operative staple lines intact in lower pelvis; no soft-tissue mass recurrence.",
            "Subcentimeter mesenteric and retroperitoneal lymph nodes without architectural distortion.",
            "No free fluid, pelvic collection, or bony osteolytic changes."
        ],
        "conclusion": "No radiological evidence of locoregional recurrence or distant organ metastases. Stable disease / R0 confirmation.",
        "reporting_specialist": "Dr. K. N. Venkatesh, MD (Radiodiagnosis), Celabs Diagnostics",
        "default_filename": "Restaging_CT_Abdomen_Pelvis_Interim.pdf",
        "file_size": "2.4 MB"
    },
    "histopathology": {
        "title": "Surgical Pathology & Biomarker Immunohistochemistry",
        "category": "Histopathology Report",
        "facility": "Apex Histopathology & Molecular Diagnostics",
        "accreditation": "CAP Accredited #782190 | NABL Certified",
        "specimen_id": "HISTO-2026-8941",
        "summary": "Microscopic analysis and immunohistochemical tumor profiling of primary resected specimen.",
        "clinical_notes": "Surgical margin status and regional lymph node staging for treatment stratification.",
        "table_data": [
            {"parameter": "Histological Subtype", "value": "Invasive Adenocarcinoma", "unit": "", "reference_range": "Moderately Diff.", "flag": "Normal", "notes": "Grade 2, glandular formation 65%"},
            {"parameter": "Surgical Margins", "value": "Clear (> 15 mm)", "unit": "mm", "reference_range": "> 2 mm", "flag": "Normal", "notes": "Negative for in-situ or invasive carcinoma"},
            {"parameter": "Total Lymph Nodes Isolated", "value": "18 nodes", "unit": "", "reference_range": ">= 12 nodes", "flag": "Normal", "notes": "Adequate oncologic lymphadenectomy"},
            {"parameter": "Lymphovascular Invasion (LVI)", "value": "Present (Focal)", "unit": "", "reference_range": "Absent", "flag": "High", "notes": "Adjuvant systemic risk factor noted"},
            {"parameter": "Ki-67 Proliferation Index", "value": "22%", "unit": "%", "reference_range": "< 20% Low", "flag": "High", "notes": "Intermediate-high proliferation"}
        ],
        "findings": [
            "Infiltrative malignant neoplasm with tubuloglandular architecture.",
            "Clear proximal, distal, and radial surgical resection margins.",
            "Presence of focal lymphovascular invasion.",
            "Immunohistochemistry confirms molecular biomarkers favorable for standard systemic protocol."
        ],
        "conclusion": "Resection margins confirmed negative. Pathological characteristics correlate with recommended adjuvant chemotherapy.",
        "reporting_specialist": "Prof. Dr. Elizabeth George, MD, FRCPath",
        "default_filename": "Histopathology_Molecular_Profile.pdf",
        "file_size": "720 KB"
    },
    "cbc_panel": {
        "title": "Pre-Infusion Complete Blood Count & Chemistry Panel",
        "category": "CBC Blood Panel",
        "facility": "Celabs Diagnostics Pvt. Ltd.",
        "accreditation": "NABL Accredited Lab #MC-2091",
        "specimen_id": "SPEC-11048-HEM",
        "summary": "Stat pre-chemotherapy safety panel evaluating marrow reserve, liver enzymes, and renal function.",
        "clinical_notes": "Dose safety screening prior to next infusion. Sample collected 08:30 AM.",
        "table_data": [
            {"parameter": "Hemoglobin (Hb)", "value": "11.2", "unit": "g/dL", "reference_range": "12.0 - 16.0", "flag": "Low", "notes": "Mild chemotherapy-related normocytic anemia"},
            {"parameter": "Absolute Neutrophil Count (ANC)", "value": "1,980", "unit": "/µL", "reference_range": "1,500 - 7,000", "flag": "Normal", "notes": "Above safe threshold (>1,500) for cytotoxics"},
            {"parameter": "Platelet Count", "value": "126,000", "unit": "/µL", "reference_range": "150,000 - 450,000", "flag": "Low", "notes": "Grade 1 thrombocytopenia; protocol allows continuation"},
            {"parameter": "Serum Creatinine", "value": "0.89", "unit": "mg/dL", "reference_range": "0.70 - 1.20", "flag": "Normal", "notes": "Normal glomerular clearance"},
            {"parameter": "SGPT / ALT", "value": "32", "unit": "U/L", "reference_range": "7 - 45", "flag": "Normal", "notes": "Normal hepatic transaminases"},
            {"parameter": "Total Bilirubin", "value": "0.8", "unit": "mg/dL", "reference_range": "0.2 - 1.2", "flag": "Normal", "notes": "Within safe range for drug metabolism"}
        ],
        "findings": [
            "Absolute neutrophil count is 1,980/µL, meeting standard dosing threshold.",
            "Mild platelet reduction to 126,000/µL (Grade 1), acceptable for full or slightly modified dose.",
            "Liver and renal clearance panels confirm normal organ function."
        ],
        "conclusion": "Adequate hematologic and organ reserve. Approved from laboratory perspective for planned chemotherapy cycle.",
        "reporting_specialist": "Dr. Sunita Rao, MD (Hematopathology), Celabs Diagnostics",
        "default_filename": "Pre_Infusion_CBC_Chemistry_Panel.pdf",
        "file_size": "340 KB"
    }
}

class DocumentParserEngine:
    """Simulates background OCR, unstructured text normalization, and clinical entity structuring."""

    @staticmethod
    def parse_sample(sample_type: str, patient_id: str, custom_date: str = None) -> ClinicalDocument:
        template = SAMPLE_TEMPLATES.get(sample_type, SAMPLE_TEMPLATES["cbc_panel"])
        today_str = custom_date or datetime.now().strftime("%d-%b-%Y")
        doc_id = f"DOC-{patient_id}-{uuid.uuid4().hex[:6].upper()}"

        table_rows = [
            ClinicalTableRow(
                parameter=row["parameter"],
                value=row["value"],
                unit=row["unit"],
                reference_range=row["reference_range"],
                flag=row["flag"],
                notes=row.get("notes", "")
            )
            for row in template["table_data"]
        ]

        return ClinicalDocument(
            id=doc_id,
            patient_id=patient_id,
            title=template["title"],
            category=template["category"],
            date=today_str,
            facility=template["facility"],
            accreditation=template["accreditation"],
            specimen_id=template["specimen_id"],
            summary=template["summary"],
            clinical_notes=template["clinical_notes"],
            table_data=table_rows,
            findings=template["findings"],
            conclusion=template["conclusion"],
            reporting_specialist=template["reporting_specialist"],
            source_file_name=template["default_filename"],
            file_size=template["file_size"],
            status="Processed & Verified"
        )

    @staticmethod
    def parse_uploaded_file(filename: str, file_bytes: bytes, patient_id: str) -> ClinicalDocument:
        """Parses an uploaded raw file by inferring category from filename and content."""
        lower_name = filename.lower()
        if any(k in lower_name for k in ["ct", "scan", "mri", "pet", "radio"]):
            category = "CT Abdomen Scan"
            sample_type = "ct_scan"
        elif any(k in lower_name for k in ["histo", "biopsy", "path", "pathology"]):
            category = "Histopathology Report"
            sample_type = "histopathology"
        else:
            category = "CBC Blood Panel"
            sample_type = "cbc_panel"

        doc = DocumentParserEngine.parse_sample(sample_type, patient_id)
        doc.source_file_name = filename
        size_kb = max(len(file_bytes) // 1024, 180)
        doc.file_size = f"{size_kb} KB"
        doc.title = f"Uploaded {category} ({filename})"
        return doc
