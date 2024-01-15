import glob
from fpdf import fpdf
from pathlib import Path

filepaths = glob.glob("TextFiles/*.txt")
pdf = fpdf.FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    pdf.add_page()
    filename = Path(filepath).stem
    with open(filepath, "r") as file:
        content = file.readline()
        print(content)
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=0, h=16, txt=filename, ln=1, border=0, align="L")
    pdf.set_font(family="Times", size=10)
    pdf.multi_cell(w=0, h=6, txt=content, border=0, align="L")
    pdf.line(10, 21, 200, 21)

pdf.output(f"PDFs/animals.pdf")

