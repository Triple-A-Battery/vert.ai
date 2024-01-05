import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://www.screener.in/screens/1336/roe/?page="
# base_url = "https://www.screener.in/screens/167969/pe-ratio/?page="

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

with open('./data/pr_roe_roa.csv', 'a', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    for page_num in range(1, 16):
        url = base_url + str(page_num)
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an exception for HTTP errors
            soup = BeautifulSoup(response.text, 'html.parser')

            tr_tags = soup.select("tr[data-row-company-id]")  # Select all tr tags with data-row-company-id attribute
            # print(tr_tags)
            for tr in tr_tags:
                td_values = tr.select("td")
                if len(td_values) > 9:  # Check if there are more than 9 td tags to avoid IndexError
                    value_pe = td_values[3].text.strip()  # Extract pe value
                    value_roe = td_values[-3].text.strip()  # Extract roe value 
                    value_roa = td_values[-4].text.strip() # Extract roa value
                    company_name = tr.select_one("td.text a").text.strip()  # Extract company name
                    # company_code = tr.select_one("td.text a")["href"].split("/")[-2].strip()  # Extract company code from href
                    
                    csvwriter.writerow([company_name, value_pe, value_roe, value_roa])
            
            print(f'[OK!!]-{page_num}')
            
        except requests.RequestException as e:
            print(f"Error fetching page {page_num}: {e}")
            continue  # Continue to the next iteration if there's an error