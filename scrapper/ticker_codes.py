import requests
import pandas as pd 

df = pd.read_csv('./data/final_data.csv')
company_names = df['company'].unique()
ticker_symbols = {}

def get_ticker(company_name):
    yfinance = "https://query2.finance.yahoo.com/v1/finance/search"
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    params = {"q": company_name, "quotes_count": 1, "country": "United States"}

    res = requests.get(url=yfinance, params=params, headers={'User-Agent': user_agent})
    data = res.json()

    company_code = data['quotes'][0]['symbol']
    return company_code

for company in company_names:
    try:
        print(1)
        ticker_symbols[company] = get_ticker(company)
        print(ticker_symbols[company])
    except:
        print(2)
        ticker_symbols[company] = "Not Found"

# Create a new DataFrame to store the results
result_df = pd.DataFrame(list(ticker_symbols.items()), columns=['Company Name', 'Ticker Symbol'])

# Write the results to a new CSV file
result_df.to_csv('./data/ticker_symbols.csv', index=False)

print("Ticker symbols written to 'ticker_symbols.csv'")

# import pandas as pd
# import yfinance as yf

# print(1)
# # Function to fetch ticker symbol for a given company name
# def get_ticker_symbol(company_name):
#     ticker = yf.Ticker(company_name)
#     return ticker.info.get('symbol')

# # Load the CSV file into a DataFrame
# df = pd.read_csv('./data/final_data.csv')

# # Extract unique company names from the DataFrame
# company_names = df['company'].unique()

# # Dictionary to store company names and their ticker symbols
# ticker_symbols = {}

# # Fetch ticker symbols for each company name
# for company in company_names:
#     try:
#         ticker_symbols[company] = get_ticker_symbol(company)
#     except:
#         ticker_symbols[company] = "Not Found"

# # Create a new DataFrame to store the results
# result_df = pd.DataFrame(list(ticker_symbols.items()), columns=['Company Name', 'Ticker Symbol'])

# # Write the results to a new CSV file
# result_df.to_csv('./data/ticker_symbols.csv', index=False)

# print("Ticker symbols written to 'ticker_symbols.csv'")
