import pandas as pd

# Creating individual Series
series1 = pd.Series([1, 2, 3, 2, 1])
series1.name = 'salamo3alikom'
series2 = pd.Series([4, 5, 6], index=["1", "2", "3"])
series3 = pd.Series([7, 8, 9])

# todo Creating a list of Series
series_list = [series1, series2, series3]
print(series1.dtype)
print(series1.size)
print(series1.name)
print(series2[0])
# Displaying the list of Series
for i, series in enumerate(series_list):
    print(f"Series {i + 1}:\n{series}\n")

    price_per_category = {
        'Fruits': 1.50,
        'Vegetables': 2.00,
        'Dairy': 3.25,
        'Meat': 5.00,
        'Grains': 1.75
    }

    # todo Creating a Series from the dictionary
    price_series = pd.Series(price_per_category)
    # Displaying the Series
    print(price_series)
    print(price_series['Fruits'])
    print(type(price_series.index))

# Dictionary representing start date deposits
start_date_deposit = {
    '2024-01-01': 1000,
    '2024-02-01': 1500,
    '2024-03-01': 2000,
    '2024-04-01': 2500,
    '2024-05-01': 3000
}

# todo Creating a Series from the dictionary
deposit_series = pd.Series(start_date_deposit)

# Calculating sum, min, and max
total_deposit = deposit_series.sum()
min_deposit = deposit_series.min()
max_deposit = deposit_series.max()
# Printing the results
print(f"Total Deposit: {total_deposit}")
print(f"Minimum Deposit: {min_deposit}")
print(f"Maximum Deposit: {max_deposit}")

print(deposit_series.idxmax())
print(deposit_series.idxmin())
print('first four ---------------------------------')
print(deposit_series.head(4))
print('last 4 ---------------------------------')
print(deposit_series.tail(4))

print('testing series string methods---------------------------------')
series_string_method = pd.Series(["heloo askjbasd, akjsdbadsd  heloo"])
print(series_string_method.str.lstrip('heloo'))
