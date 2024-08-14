import os

from matplotlib import pyplot as plt

import numpy as np
import pandas as pd
# Reading the first CSV file
csv_file = 'files/Marina Shopping - Long term unit IDs.csv'
df1 = pd.read_csv(csv_file, engine='python', usecols=['Unit ID'])
csv_data = df1.copy()
# Display the DataFrame
print(df1)
print(type(df1))
df1_squeeze: pd.Series = csv_data.squeeze(True)
print(type(df1_squeeze))
print('-------------------------')
# print(df1_squeeze.unique())
print(df1_squeeze.array)
print('-------------------------')

# Simple dictionary
data = {
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [30, 25, 35]
}

# Convert dictionary to DataFrame
df2 = pd.DataFrame(data)

# Set 'id' as the index
df2.set_index('id', inplace=True)

# Display the DataFrame
print(df2)
print('-------------------------')

# Reading the second CSV file using pandas
filename2 = 'files/Lending-Company-Numeric-Data-NAN.csv'
df3 = pd.read_csv(filename2, engine='python')

# Display the DataFrame
print(df3)
print(type(df3))
print('-------------------------')
# If you still want to convert it to a NumPy array, you can do it as follows:
numeric_data1, numeric_data2, numeric_data3 = np.loadtxt(filename2, delimiter=';', dtype=np.str_,
                                                         usecols=(0, 1, 2), unpack=True)

# Display the NumPy array
print(numeric_data1)
print(numeric_data2)
print(numeric_data3)
# print(type(numeric_data))

if not os.path.exists(csv_file):
    df1.to_csv(csv_file)
print('-------------------------')

marina_shopping = np.genfromtxt(csv_file, delimiter=',', dtype=np.str_)
# todo save
if not os.path.exists('save_marina_shopping.npy'): np.save('save_marina_shopping', marina_shopping)
loaded_data = np.load('save_marina_shopping.npy')
print(loaded_data)

print('-------------------------')
# todo savez
if not os.path.exists('savez_save_marina_shopping.npz'): np.savez('savez_save_marina_shopping',
                                                                  marina_shopping=marina_shopping,
                                                                  loaded_data=loaded_data)
loaded_data2 = np.load('savez_save_marina_shopping.npz')
print(loaded_data2['marina_shopping'])
print(loaded_data2.files)

print('-------------------------')
# todo savetxt
if not os.path.exists('marina_shopping.txt'):  np.savetxt('marina_shopping.txt', marina_shopping, fmt='%s',
                                                          delimiter=',')
loaded_text_data = np.loadtxt('marina_shopping.txt', delimiter=',', dtype=np.str_)
print(loaded_text_data)
print(np.array_equal(loaded_text_data, marina_shopping))

print('-------------------------')
import pandas as pd

# Create a pandas Series
data = pd.Series({'Product A': 11293, 'Product B': 21081, 'Product C': 3897, 'Product D': 4751, 'Product E': 5123})
print(data.sort_values())
# Convert to NumPy array using .to_numpy()
numpy_array_1 = data.to_numpy()
print("Using .to_numpy():", numpy_array_1)

# Convert to NumPy array using .values
numpy_array_2 = data.values
print("Using .values:", numpy_array_2)

# Convert to an array using .array
pandas_array = data.array
print("Using .array:", pandas_array)

# Check if .to_numpy() and .values yield the same result
print("Are .to_numpy() and .values equal?", (numpy_array_1 == numpy_array_2).all())

# Check if .array is equal to .to_numpy()
print("Are .array and .to_numpy() equal?", (pandas_array == numpy_array_1).all())
print(type(numpy_array_1))
print(type(numpy_array_2))
print(type(pandas_array))
