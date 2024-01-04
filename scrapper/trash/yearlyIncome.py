import requests
from bs4 import BeautifulSoup
import time
import csv

base_url = "https://companiesmarketcap.com/page/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

with open('yearlyIncome.csv', 'a', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    for page_num in range(1, 81):
        url = base_url + str(page_num) + '/'
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an exception for HTTP errors
            soup = BeautifulSoup(response.text, 'html.parser')

            td_tags = soup.find_all("td", class_="td-right")
            
            for td in td_tags:
                if td.text.strip().endswith("T") or td.text.strip().endswith("B") or td.text.strip().endswith("M"):
                    market_cap = td.text.strip()
                    company_name = td.find_previous_sibling("td", class_="name-td").find("div", class_="company-name").text.strip()
                    company_code = td.find_previous_sibling("td", class_="name-td").find("div", class_="company-code").text.strip()
                    
                    csvwriter.writerow([company_name, company_code, market_cap])
            
            print(f'[OK!!]-{page_num}')
            
        except requests.RequestException as e:
            print(f"Error fetching page {page_num}: {e}")
            continue  # Continue to the next iteration if there's an error

        # time.sleep(2)