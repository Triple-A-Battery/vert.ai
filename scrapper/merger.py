import pandas as pd

# Load the CSV files into DataFrames
esg_df = pd.read_csv('./data/esg.csv')
pe_roe_df = pd.read_csv('./trash/pe_roe.csv')
open_df = pd.read_csv('./data/open.csv')

# Create an empty list to store the merged data
merged_data = []

# Loop through each row in the pe_roe DataFrame
for _, row in pe_roe_df.iterrows():
    company_name = row['company']
    
    # Find a matching company name from esg_df (even if it's slightly different)
    # matched_row = esg_df[esg_df['company'].str.contains(company_name, case=False, na=False)]
    matched_row = esg_df[esg_df['company'].str.contains(company_name, case=False, na=False, regex=False)]

    # If a match is found, extract the relevant data
    if not matched_row.empty:
        stock_name = matched_row['stock_name'].iloc[0]
        esg_rating = matched_row['esg_rating'].iloc[0]
        pe_ratio = row['pe_ratio']
        roe = row['roe']
        
        # Find the open value from open_df
        open_value = open_df.loc[open_df['company'] == company_name, 'open'].iloc[0] if company_name in open_df['company'].values else None
        
        # Append the data to the merged list
        merged_data.append([company_name, stock_name, esg_rating, pe_ratio, roe, open_value])

# Convert the merged data to a DataFrame
merged_df = pd.DataFrame(merged_data, columns=['company', 'stock_name', 'esg_rating', 'pe_ratio', 'roe', 'open'])

# Write the merged DataFrame to a new CSV file
merged_df.to_csv('./data/final_data.csv', index=False)

print("Merged data written to 'final_data.csv'")