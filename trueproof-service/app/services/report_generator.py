from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import hashlib
import os

def generate_pdf_report(file_path, result_data, output_path):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "TrueProof AI Forensic Verification Report")

    c.setFont("Helvetica", 12)
    y = height - 100

    def draw_line(label, value):
        nonlocal y
        c.drawString(50, y, f"{label}: {value}")
        y -= 20

    with open(file_path, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()

    draw_line("File Name", os.path.basename(file_path))
    draw_line("SHA-256 Hash", sha)
    draw_line("Scan Date", datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"))
    draw_line("Manipulation Score", f"{result_data['manipulation_score']}")
    draw_line("Verdict", result_data["verdict"])
    draw_line("Model Used", result_data["model"])

    c.save()
    return output_path