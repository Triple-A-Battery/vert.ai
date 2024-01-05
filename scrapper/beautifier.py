import pandas as pd

# Read the CSV file
df = pd.read_csv('./data/final_data.csv')

# Remove commas from the 'open' column and convert it to numeric first
df['open'] = df['open'].str.replace(',', '').astype(float).astype(float)

# Save the modified DataFrame to a new CSV file
df.to_csv('./data/final_data2.csv', index=False)

print("Modified data saved to 'final_data2.csv'")
