import yfinance as yf
import pandas as pd

# Read ticker symbols from CSV into a DataFrame
df = pd.read_csv("./ticker_symbols.csv")


# Define a function to fetch data for a specific company
def fetch_data(company_ticker):
    filtered_df = df[df["ticker"] == company_ticker]
    if not filtered_df.empty:
        stock = yf.Ticker(company_ticker)

        data = {}
        # Get stock info
        information = stock.info
        data["shortName"] = information.get("shortName", "N/A")
        data["industry"] = information.get("industry", "N/A")
        data["country"] = information.get("country", "N/A")
        data["currency"] = information.get("currency", "N/A")
        data["currentPrice"] = information.get("currentPrice", "N/A")
        data["currentRatio"] = information.get("currentRatio", "N/A")
        data["dayHigh"] = information.get("dayHigh", "N/A")
        data["dayLow"] = information.get("dayLow", "N/A")
        data["debtToEquity"] = information.get("debtToEquity", "N/A")
        return [data]
    else:
        return []
