import yfinance as yf
import csv

# Read ticker symbols from CSV
companies = []
with open("../data/ticker_symbols.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        companies.append(row)

return_data = []


# Fetch and print information for each company
def fetch_data(company_name):
    for company in companies:
        if company == company_name:
            ticker_symbol = company["ticker"]
            stock = yf.Ticker(ticker_symbol)

            data = {}
            # Get stock info
            data[information] = stock.info
            data[shortName] = information.get("shortName", "N/A")
            data[industry] = information.get("industry", "N/A")
            data[country] = information.get("country", "N/A")
            data[currency] = information.get("currency", "N/A")
            data[currentPrice] = information.get("currentPrice", "N/A")
            data[currentRatio] = information.get("currentRatio", "N/A")
            data[dayHigh] = information.get("dayHigh", "N/A")
            data[dayLow] = information.get("dayLow", "N/A")
            data[debtToEquity] = information.get("debtToEquity", "N/A")
            return_data.append(data)

    return return_data
