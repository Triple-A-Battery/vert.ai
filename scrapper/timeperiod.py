import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Read ticker symbols from CSV
tickers = {}
with open('./data/ticker_symbols.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    tickers = {row[0]: row[1] for row in reader}

base_url = "https://finance.yahoo.com/quote/{}/history?p={}"

# Initialize the WebDriver
driver = webdriver.Chrome()

for company, ticker in tickers.items():
    print(f"Fetching data for {company} - {ticker}")
    
    driver.get(base_url.format(ticker, ticker))
    
    try:
        # Wait for an element that indicates the page is loaded.
        wait = WebDriverWait(driver, 20)  # Increased wait time
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#YDC-SecondaryNav')))
        
        # Find all table rows
        # rows = driver.find_elements(By.CSS_SELECTOR, 'tr.BdT.Bdc($seperatorColor).Ta(end).Fz(s).Whs(nw)')
        rows = driver.find_elements(By.CLASS_NAME, 'tr.BdT.Bdc\\($seperatorColor\\).Ta\\(end\\).Fz\\(s\\).Whs\\(nw\\)')
        
        # Prepare data to write to CSV
        data = []
        counter = 0 
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, 'td')
            date = cols[0].text
            open_value = cols[1].text
            high = cols[2].text
            low = cols[3].text
            close = cols[4].text
            adj_close = cols[5].text
            volume = cols[6].text.replace(',', '')
            
            data.append([company, date, open_value, high, low, close, adj_close, volume])
            counter += 1 
            
            if counter > 10:
                break

        # Write to CSV
        with open('./data/timeperiod.csv', 'a', newline='', encoding='utf-8') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(data)

    except Exception as e:
        print(f"Error fetching data for {company} - {ticker}: {e}")

print("Data written to ./data/timeperiod.csv")