from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
from app.services.report_generator import generate_pdf_report
import tempfile
import shutil

router = APIRouter()

@router.post("/report")
async def generate_report(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        shutil.copyfileobj(file.file, tmp_file)
        tmp_path = tmp_file.name

    result_data = {
        "manipulation_score": 0.83,
        "verdict": "Likely Manipulated",
        "model": "MockModel-v1",
    }

    output_pdf = tmp_path + "_report.pdf"
    generate_pdf_report(tmp_path, result_data, output_pdf)

    return FileResponse(output_pdf, filename="TrueProof_Report.pdf", media_type="application/pdf")