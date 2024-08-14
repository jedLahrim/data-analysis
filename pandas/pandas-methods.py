import pandas as pd

# todo Read data from the CSV file
csv_file = '../files/simple_data.csv'
df = pd.read_csv(csv_file, engine='python')

# todo Display the first few rows of the DataFrame
print("Head of the DataFrame:")
print(df.head())

# todo Get a concise summary of the DataFrame
print("\nInfo of the DataFrame:")
print(df.info())

# todo Generate descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# todo Remove rows with missing values (there are none in this example, so the DataFrame remains unchanged)
df_clean = df.dropna()
print("\nDataFrame after dropping NA values:")
print(df_clean)

# todo Fill missing values (no missing values here, so the DataFrame remains unchanged)
df_filled = df.fillna(0)
print("\nDataFrame after filling NA values with 0:")
print(df_filled)

# todo Drop a column
df_dropped = df.drop('Gender', axis=1)
print("\nDataFrame after dropping the 'Gender' column:")
print(df_dropped)

# todo Rename columns
df_renamed = df.rename(columns={'Salary': 'Annual Salary'})
print("\nDataFrame after renaming the 'Salary' column to 'Annual Salary':")
print(df_renamed)

# todo Sort by the 'Age' column
df_sorted = df.sort_values(by='Age')
print("\nDataFrame sorted by 'Age':")
print(df_sorted)

# todo Group by 'Department' and calculate the mean salary
grouped_df = df.groupby('Department').mean(numeric_only=True)
print("\nMean salary by Department:")
print(grouped_df)

# todo Merge two DataFrames
df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value': [4, 5, 6]})

merged_df = pd.merge(df1, df2, on='key', how='inner')
print(merged_df)

# todo Create a pivot table
pivot_table = df.pivot_table(values='Salary', index='Department', columns='Gender', aggfunc='mean')
print("\nPivot table of mean Salary by Department and Gender:")
print(pivot_table)

# todo Apply a function to a column (double the salaries)
df['Doubled Salary'] = df['Salary'].apply(lambda x: x * 2)
print("\nDataFrame with 'Doubled Salary' column:")
print(df)

# 1 todo Select by row and column indices
subset_df = df.iloc[0:4, 0:5]
print("\nPart1 Subset of DataFrame using iloc:")
print(subset_df)

# 2 todo Select by row and column indices
subset_df = df.iloc[[2, 5], :]
print("\nPart2 Subset of DataFrame using iloc:")
print(subset_df)

# todo Select by row and column labels
subset_df = df.loc[0:2, ['Name', 'Age', 'Gender', 'Salary']]
print("\nSubset of DataFrame using loc:")
print(subset_df)

# todo Detect missing values
missing_values = df.isnull()
print("\nMissing values in DataFrame:")
print(missing_values)

# todo Detect non-missing values
non_missing_values = df.notnull()
print("\nnon-Missing values in DataFrame:")
print(non_missing_values)

# todo Count unique values in 'Department' column
value_counts = df['Department'].value_counts()
print("\nValue counts in 'Department' column:")
print(value_counts)

# todo Append a new row to the DataFrame
# New row to append
new_row = pd.DataFrame(
    {'Name': ['Hank'], 'Age': [40], 'Gender': ['Male'], 'Department': ['Marketing'], 'Salary': [90000]})

# todo Append the new row to the DataFrame using pd.concat
# here we use concat instead of append because append method in last panda version's deprecated
df_appended = pd.concat([df, new_row], ignore_index=True)
print("\nDataFrame after appending a new row:")
print(df_appended)

# todo Concatenate two DataFrames
df1 = pd.DataFrame({'Name': ['Ivy'], 'Age': [23], 'Gender': ['Female'], 'Department': ['HR'], 'Salary': [50000]})
df2 = pd.DataFrame(
    {'Name': ['Jack'], 'Age': [28], 'Gender': ['Male'], 'Department': ['Engineering'], 'Salary': [75000]})

df_concatenated = pd.concat([df1, df2])
print("\nConcatenated DataFrame:")
print(df_concatenated)
