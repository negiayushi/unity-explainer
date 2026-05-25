# ============================================================
# report.py
# This file creates a professional PDF report card
# that the genetic counselor can print or email to the patient.
# It uses a library called fpdf2 to build the PDF from scratch.
# ============================================================

from fpdf import FPDF
from datetime import datetime


def clean_text(text: str) -> str:
    """Replace special characters that Helvetica font cannot handle."""
    replacements = {
        "\u2014": "-",   # em dash —
        "\u2013": "-",   # en dash –
        "\u2018": "'",   # left single quote '
        "\u2019": "'",   # right single quote '
        "\u201c": '"',   # left double quote "
        "\u201d": '"',   # right double quote "
        "\u2026": "...", # ellipsis …
        "\u00e9": "e",   # é
        "\u00f3": "o",   # ó
        "\u00ed": "i",   # í
        "\u00fa": "u",   # ú
        "\u00e1": "a",   # á
        "\u00f1": "n",   # ñ
    }
    for char, replacement in replacements.items():
        text = text.replace(char, replacement)
    return text


class PatientReportPDF(FPDF):
    """
    A custom PDF class. We extend FPDF so we can add
    our own header and footer to every page automatically.
    """

    def header(self):
        """This runs automatically at the top of every page."""

        # Dark teal background bar (BillionToOne brand colors)
        self.set_fill_color(10, 100, 80)
        self.rect(0, 0, 210, 30, "F")

        # Company name (white text)
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(255, 255, 255)
        self.set_xy(10, 6)
        self.cell(100, 8, "BillionToOne", ln=0)

        # Report title (white text, right side)
        self.set_font("Helvetica", "", 10)
        self.set_xy(10, 16)
        self.cell(
            190, 8,
            "Patient Result - Plain Language Summary",
            align="C",
        )

        # Move cursor below the header bar
        self.set_xy(10, 38)

    def footer(self):
        """This runs automatically at the bottom of every page."""
        self.set_y(-20)
        self.set_font("Helvetica", "I", 7.5)
        self.set_text_color(150, 150, 150)
        self.multi_cell(
            0, 4,
            "This summary is prepared to help you understand your result in plain language. "
            "It does not replace a conversation with your genetic counselor or physician. "
            f"Generated on {datetime.now().strftime('%B %d, %Y')}  |  Page {self.page_no()}",
            align="C",
        )


def generate_pdf(
    patient_name: str,
    condition: str,
    result: str,
    risk: str,
    product: str,
    language: str,
    explanation: str,
    output_path: str,
):
    """
    Takes all the patient info and the AI-generated explanation,
    and creates a clean PDF file saved at output_path.
    """

    # Clean special characters from all text fields before rendering
    patient_name = clean_text(patient_name)
    condition    = clean_text(condition)
    result       = clean_text(result)
    risk         = clean_text(risk)
    product      = clean_text(product)
    language     = clean_text(language)
    explanation  = clean_text(explanation)

    pdf = PatientReportPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=25)

    # ── Patient info summary box ──────────────────────────────
    # Light gray background box
    pdf.set_fill_color(245, 245, 243)
    pdf.set_draw_color(200, 200, 195)
    pdf.rect(10, 38, 190, 42, "FD")

    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(30, 30, 30)
    pdf.set_xy(15, 42)
    pdf.cell(85, 7, f"Patient:  {patient_name}", ln=0)
    pdf.cell(95, 7, f"Test product:  {product}", ln=1)

    pdf.set_xy(15, 50)
    pdf.set_font("Helvetica", "", 10)
    pdf.cell(85, 7, f"Condition:  {condition[:45]}", ln=0)
    pdf.cell(95, 7, f"Language:  {language}", ln=1)

    pdf.set_xy(15, 58)
    pdf.cell(85, 7, f"Result:  {result}", ln=0)
    pdf.cell(95, 7, f"Risk / probability:  {risk}", ln=1)

    # ── Divider line ─────────────────────────────────────────
    pdf.set_y(85)
    pdf.set_draw_color(10, 100, 80)
    pdf.set_line_width(0.5)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(5)

    # ── Main explanation text ─────────────────────────────────
    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(35, 35, 35)
    pdf.set_line_width(0.2)

    # multi_cell handles automatic line wrapping
    pdf.multi_cell(0, 7, explanation)

    pdf.ln(6)

    # ── Bottom note ───────────────────────────────────────────
    pdf.set_draw_color(10, 100, 80)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(4)

    pdf.set_font("Helvetica", "I", 9)
    pdf.set_text_color(80, 80, 80)
    pdf.multi_cell(
        0, 5,
        "Questions about your result? BillionToOne offers complimentary genetic "
        "counseling calls. Contact your healthcare provider or visit unityscreen.com.",
    )

    # Save the PDF file to disk
    pdf.output(output_path)