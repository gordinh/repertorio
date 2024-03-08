import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("./invoices/*.xlsx")

for filepath in filepaths:
  pdf = FPDF(orientation="P", unit="mm", format="A4")
  pdf.add_page()
  
  
  filename = Path(filepath).stem
  invoice_nr, invoice_date = filename.split("-")
  
  pdf.set_font(family="Times", size=16, style="B")
  pdf.cell(w=50, h=8, txt=f"Invoice Nr.{invoice_nr}", ln=1)

  pdf.set_font(family="Times", size=16, style="B")
  pdf.cell(w=50, h=8, txt=f"Date {invoice_date}", ln=1)
  
  df = pd.read_excel(filepath, sheet_name="Sheet 1")

  # Add a header
  pdf.set_font(family="Times", size=10, style="B")
  pdf.set_text_color(80, 80, 80)

  for column in list(df.columns):
    column_normalized = column.replace('_', ' ').title()
    pdf.cell(w=(len(column_normalized) + 15), h=8, txt=str(column_normalized), border=1)

  pdf.cell(w=50, h=8, txt="", ln=1)
  # Add rows

  for index, row in df.iterrows():
    pdf.set_font(family="Times", size=10)

    pdf.cell(w=25, h=8, txt=str(row['product_id']), border=1)
    pdf.cell(w=27, h=8, txt=str(row['product_name']), border=1)
    pdf.cell(w=31, h=8, txt=str(row['amount_purchased']), border=1)
    pdf.cell(w=29, h=8, txt=str(row['price_per_unit']), border=1)
    pdf.cell(w=26, h=8, txt=str(row['total_price']), border=1, ln=1)
  
  total_sum = str(df["total_price"].sum())
  
  pdf.cell(w=25, h=8, txt="", border=1)
  pdf.cell(w=27, h=8, txt="", border=1)
  pdf.cell(w=31, h=8, txt="", border=1)
  pdf.cell(w=29, h=8, txt="", border=1)
  pdf.cell(w=26, h=8, txt=total_sum, border=1, ln=1)

  # Add total sum sentence
  pdf.cell(w=29, h=8, txt=f"The total price is {total_sum}", ln=1)

  # Add company name and logo
  pdf.cell(w=29, h=8, txt=f"PythonHow")
  pdf.image("./pythonhow.png", w=10)


  pdf.output(f"PDFs/Invoice_{invoice_nr}.pdf")
