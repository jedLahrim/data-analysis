# Sample JSON string
import os

import pandas as pd

json_file = 'files/Lending-company.json'

# Read JSON string into a DataFrame
df = pd.read_json(json_file, engine='ujson')

# Display the DataFrame
print(df)

if not os.path.exists(json_file):
    df.to_json(json_file)
