import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://finance.yahoo.com/quote/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Read ticker symbols and company names
ticker_data = []
with open('./data/ticker_symbols.csv', 'r', newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip header row
    for row in csvreader:
        ticker_data.append(row)

# Write to open.csv
with open('./data/open.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Company', 'OPEN Value'])  # Header
    
    for company_name, ticker_symbol in ticker_data:
        url = base_url + ticker_symbol
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an exception for HTTP errors
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find OPEN value
            open_value_tag = soup.find("td", {"data-test": "OPEN-value"})
            if open_value_tag:
                open_value = open_value_tag.text.strip()
                csvwriter.writerow([company_name, open_value])
            else:
                csvwriter.writerow([company_name, 'Not Found'])
                
            print(f'[OK!!] - {company_name}')
            
        except requests.RequestException as e:
            print(f"Error fetching data for {company_name}: {e}")