import pandas as pd
import glob
import openpyxl

filepaths = glob.glob("invoices/*.xlsx")
print(filepaths)

for filepath in filepaths:
    print(filepath)
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(df)
    print("************************")
