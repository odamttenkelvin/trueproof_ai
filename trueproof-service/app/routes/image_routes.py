from fastapi import APIRouter, UploadFile, File
from app.services.image_analyzer import analyze_image

router = APIRouter()

@router.post("/analyze/image")
async def analyze_uploaded_image(file: UploadFile = File(...)):
    contents = await file.read()
    result = analyze_image(contents)
    return {"status": "ok", "prediction": result}