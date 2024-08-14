import json

import pandas as pd
import requests
from openpyxl import load_workbook

api_url = 'https://api.restful-api.dev/objects?id=3&id=5&id=10'
try:
    response = requests.get(api_url)
    data = response.json()
    print(data)
    pretty_json = json.dumps(data, indent=4)

    print(pretty_json)
except  requests.RequestException as e:
    print(f'Connection Error {e}')

print('-------------------------------------')
base_url = 'https://itunes.apple.com/search'
# url = base_url + '?term=the+beatles&country=us'
response = requests.get(base_url, params={'term': 'the+beatles', 'country': 'us'})
data = response.json()
pretty_json = json.dumps(data, indent=4)
print(pretty_json)
print('-------------------------------------')
df = pd.DataFrame(data['results'])
df.set_index('artistId', inplace=True)

# Specify the Excel file path
excel_file = 'songs_info.xlsx'

# Save the DataFrame to Excel
df.to_excel(excel_file, engine='openpyxl')

# Load the workbook and select the active worksheet
wb = load_workbook(excel_file)
ws = wb.active

# Adjust the column widths
for column in ws.columns:
    max_length = 0
    column = [cell for cell in column]
    for cell in column:
        try:
            if len(str(cell.value)) > max_length:
                max_length = len(str(cell.value))
        except:
            pass
    adjusted_width = (max_length + 2)  # Adding some padding
    ws.column_dimensions[column[0].column_letter].width = adjusted_width

# Save the adjusted workbook
wb.save(excel_file)
