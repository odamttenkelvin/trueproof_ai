from fastapi import FastAPI
from app.routes import image_routes, audio_routes, report_routes

app = FastAPI(title="TrueProof AI")

app.include_router(image_routes.router)
app.include_router(audio_routes.router)
app.include_router(report_routes.router)