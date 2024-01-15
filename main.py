import pandas as pd
import glob
from fpdf import fpdf
from datetime import datetime
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    pdf = fpdf.FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")[0:2]

    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=0, h=8, border=0, txt=f"Invoice nr: {invoice_nr}", ln=1, align="L")

    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=0, h=8, border=0, txt=f"Date: {date}", ln=1, align="L")

    pdf.output(f"PDFs/{filename}.pdf")

