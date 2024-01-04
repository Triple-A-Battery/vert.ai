import requests
from bs4 import BeautifulSoup
import time
import csv

base_url = "https://www.sustainalytics.com/sustapi/companyratings/getcompanyratings"

headers = {
    "accept": "*/*",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
}

# Open the CSV file in append mode and create a CSV writer object
with open('esg.csv', 'a', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Loop through the desired range of pages
    for page_num in range(1, 2):  # Adjust the range accordingly
        payload = {
            "industry": "",
            "rating": "",
            "filter": "",
            "page": page_num,
            "pageSize": 13770,
            "resourcePackage": "Sustainalytics",
        }

        response = requests.post(base_url, headers=headers, data=payload)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all company rows
        company_rows = soup.find_all("div", class_="company-row d-flex")

        for row in company_rows:
            company_name = row.find("a", class_="primary-color d-block js-fix-path").text.strip()
            esg_value = row.find("div", class_="col-2").text.strip()
            small_data = row.find("small").text.strip() if row.find("small") else ""

            # Write the fetched data to the CSV file
            csvwriter.writerow([company_name, esg_value, small_data])

        time.sleep(2)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# import logging
# logging.basicConfig(level=logging.INFO)

# # Initialize the Chrome WebDriver
# driver = webdriver.Chrome()
# driver.get("https://www.sustainalytics.com/esg-ratings")

# try:
#     wait = WebDriverWait(driver, 30)
#     company_name = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='company-row d-flex']//div[@class='w-50']//a[@class='primary-color d-block js-fix-path']")))
#     company_esg = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='company-row d-flex']")))

#     for name, esg in zip(company_name, company_esg):
#         ele = esg.find_elements(By.CSS_SELECTOR, "div.col-2")
        
#         for element in ele:
#             col_2_text = element.text
#             print(f"[{name.text}] - {col_2_text}")

# except Exception as e:
#     print(f"An error occurred: {e}")

# finally:
#     driver.quit()