from fastapi import APIRouter
from app.services.pdf_generator import generate_pdf
from app.services.blockchain_logger import log_to_blockchain

router = APIRouter()

@router.get("/report/pdf")
async def get_report():
    pdf_path = generate_pdf()
    return {"report": pdf_path}

@router.post("/report/hash")
async def log_hash():
    response = log_to_blockchain("example_hash_value")
    return response