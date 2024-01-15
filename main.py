import pandas as pd
import glob
from fpdf import fpdf
from datetime import datetime
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:

    pdf = fpdf.FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")[0:2]

    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=0, h=8, border=0, txt=f"Invoice nr: {invoice_nr}", ln=1, align="L")

    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=0, h=8, border=0, txt=f"Date: {date}", ln=1, align="L")

    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    # Add Header
    columns = list(df.columns)
    columns = [column.replace("_", " ").title() for column in columns]
    pdf.set_font(family="Times", size=10, style="B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=70, h=8, txt=columns[1], border=1)
    pdf.cell(w=30, h=8, txt=columns[2], align="R", border=1)
    pdf.cell(w=30, h=8, txt=columns[3], align="R", border=1)
    pdf.cell(w=30, h=8, txt=columns[4], align="R", border=1, ln=1)

    total = 0
    for index, row in df.iterrows():
        total += row["total_price"]
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=70, h=8, txt=row["product_name"], border=1)
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]), align="R", border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), align="R", border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), align="R", border=1, ln=1)

    pdf.set_font(family="Times", size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=70, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", align="R", border=1)
    pdf.cell(w=30, h=8, txt="", align="R", border=1)
    pdf.cell(w=30, h=8, txt=str(total), align="R", border=1, ln=1)

    # Add total
    pdf.set_font(family="Times", size=10, style="B")
    pdf.cell(w=30, h=8, txt=f"The total price is: {total}", ln=1)

    # Add name
    pdf.set_font(family="Times", size=10, style="B")
    pdf.cell(w=25, h=8, txt=f"goks-pdf-convertor", ln=1)

    pdf.output(f"PDFs/{filename}.pdf")

