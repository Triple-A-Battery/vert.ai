import yfinance as yf
import csv

# Read ticker symbols from CSV
companies = []
with open('../data/ticker_symbols.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        companies.append(row)

# Fetch and print information for each company
for company in companies:
    ticker_symbol = company['ticker']
    stock = yf.Ticker(ticker_symbol)

    # Get stock info
    information = stock.info
    shortName = information.get('shortName', 'N/A')  
    industry = information.get('industry', 'N/A')  
    country = information.get('country', 'N/A')  
    currency = information.get('currency', 'N/A')  
    currentPrice = information.get('currentPrice', 'N/A')  
    currentRatio = information.get('currentRatio', 'N/A')  
    dayHigh = information.get('dayHigh', 'N/A')  
    dayLow = information.get('dayLow', 'N/A')  
    debtToEquity = information.get('debtToEquity', 'N/A')  

    print(shortName, industry, country, currency, currentPrice, currentRatio, dayHigh, dayLow, debtToEquity)    
    print("-" * 50)  # Separator for better visibility
