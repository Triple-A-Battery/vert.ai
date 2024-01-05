import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://companieearmarketcap.com/top-companies-by-pe-ratio/page/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

with open('pe_ratio.csv', 'a', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    for page_num in range(1, 81):
        url = base_url + str(page_num) + '/'
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an exception for HTTP errors
            soup = BeautifulSoup(response.text, 'html.parser')

            tr_tags = soup.find_all("tr")
            # print(tr_tags) 
            for tr in tr_tags:
                td_tag = tr.find("td", class_="td-right")
                
                if td_tag and td_tag.text.strip():  # Check if the td tag exists and contains text
                    company_name = tr.find("div", class_="company-name").text.strip()
                    company_code = tr.find("div", class_="company-code").text.strip()
                    
                    csvwriter.writerow([company_name, company_code, td_tag.text.strip()])
            
            print(f'[OK!!]-{page_num}')
            
        except requests.RequestException as e:
            print(f"Error fetching page {page_num}: {e}")
            continue  # Continue to the next iteration if there's an error

        # time.sleep(2)