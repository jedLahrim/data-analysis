import pandas as pd

# Load the data
data = pd.read_csv('files/Marina Shopping - Long term unit IDs.csv')
print(data.dtypes)
# Squeeze the DataFrame to a Series
marina_shopping_data: pd.Series = data.squeeze()
marina_shopping_data.head()
# Sort the Series values
sorted_data = marina_shopping_data.sort_values(by=['GLA'], ascending=False)
# Print the sorted values
print(sorted_data)
print(marina_shopping_data.index)
print(sorted_data.sort_index(ascending=False))
# print(marina_shopping_data.head().to_numpy())
