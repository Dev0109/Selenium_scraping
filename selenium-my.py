import sys
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

import time 
# from selenium.webdriver.common.action_chains import ActionChains

import pandas as pd
#import openpyxl

product_links = []
product_names = []
product_prices = []
product_descriptions = []

options = Options()
options.add_argument("start-maximized")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) #open chrome

for page in range(1, 2): #only 1 page(if you want to need all pages, range(1, end page number))
	page_url = "https://www.bradburnhome.com/collections/casual?page=" + str(page)
	print(page) #print into console
    
	driver.get(page_url)

	products = driver.find_elements(By.CLASS_NAME, "eight")
	print(len(products))

	
	for i in range(len(products)):
		product_link = products[i].find_element(By.TAG_NAME, 'a').get_attribute('href')
		print(product_link)
		product_links.append(product_link)

for i in range(2):
	driver.get(product_links[i])
	product_name = driver.find_element(By.CLASS_NAME, "product_name").get_attribute('innerHTML')
	product_names.append(product_name)

	product_price = driver.find_element(By.CLASS_NAME, "money").get_attribute('innerHTML')
	product_prices.append(product_price)

	product_description_driver = driver.find_element(By.CLASS_NAME, "description")
	product_description = product_description_driver.find_element(By.TAG_NAME, 'p').get_attribute('innerHTML')
	product_descriptions.append(product_description)

	product_table = product_description_driver.find_element(By.TAG_NAME, 'table')
	product_table_rows = product_table.find_elements(By.TAG_NAME, 'tr')


	# for index in range(len(product_table_rows)):
	# 	product_table_cols = product_table_rows[index].find_elements(By.TAG_NAME, 'td')
	# 	product_table_col_name = product_table_cols[0].text
	# 	product_table_col_content = product_table_cols[1].text


	
#product_titles.append(product_title)
print("okay")
df = pd.DataFrame({'product_name': product_names, 'product_price': product_prices, 'product_description': product_descriptions})  # Create a DF with the lists

with pd.ExcelWriter('output.xlsx') as writer:
     df.to_excel(writer, sheet_name='Sheet1')

print("yes")
