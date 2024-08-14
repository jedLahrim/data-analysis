import inspect
import os

import pandas as pd

excel_file = 'files/Lending-company.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file, engine='openpyxl')

# Display the DataFrame
print(df)

if '__file__' in locals():
    fx = inspect.getframeinfo(inspect.currentframe())[0]
else:
    fx = '__file__'

os_dir = os.path.dirname(os.path.abspath(fx))
print(os_dir)

if not os.path.exists(excel_file):
    df.to_excel(excel_file, index=False)
