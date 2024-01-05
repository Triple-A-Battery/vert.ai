import pandas as pd
import yfinance as yf

# Function to fetch ticker symbol for a given company name
def get_ticker_symbol(company_name):
    ticker = yf.Ticker(company_name)
    return ticker.info.get('symbol')

# Load the CSV file into a DataFrame
df = pd.read_csv('./data/final_data.csv')

# Extract unique company names from the DataFrame
company_names = df['company'].unique()

# Dictionary to store company names and their ticker symbols
ticker_symbols = {}

# Fetch ticker symbols for each company name
for company in company_names:
    try:
        ticker_symbols[company] = get_ticker_symbol(company)
    except:
        ticker_symbols[company] = "Not Found"

# Create a new DataFrame to store the results
result_df = pd.DataFrame(list(ticker_symbols.items()), columns=['Company Name', 'Ticker Symbol'])

# Write the results to a new CSV file
result_df.to_csv('./data/ticker_symbols.csv', index=False)

print("Ticker symbols written to 'ticker_symbols.csv'")
