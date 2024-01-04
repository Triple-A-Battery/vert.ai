import pandas as pd

# Load the CSV files into DataFrames
df1 = pd.read_csv('esg.csv')
df2 = pd.read_csv('roe.csv')
df3 = pd.read_csv('yearlyIncome.csv')

# Convert the company column to lowercase for easier matching
df1['company_lower'] = df1['company'].str.lower()
df2['company_lower'] = df2['company'].str.lower()
df3['company_lower'] = df3['company'].str.lower()

# Merge DataFrames based on the company_lower column
merged_df = pd.merge(df1, df2, on='company_lower', how='outer')
merged_df = pd.merge(merged_df, df3, on='company_lower', how='outer')

# Drop the company_lower column as it's no longer needed
merged_df.drop(columns=['company_lower'], inplace=True)

# Write the merged DataFrame to a new CSV file
merged_df.to_csv('merged_file.csv', index=False)

print("Merged data written to 'merged_file.csv'")