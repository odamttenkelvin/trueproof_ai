from fpdf import FPDF
import os

def generate_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="TrueProof AI Report", ln=True)
    pdf.output("outputs/reports/report.pdf")
    return "outputs/reports/report.pdf"