import numpy as np
import pandas as pd
from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\User\chromedriver.exe")
driver.implicitly_wait(30)
driver.get('https://www.barchart.com/economy/interest-rates')
df = pd.read_html(driver.find_element_by_id("main-content-column").get_attribute('outerHTML'))
t = 1
for x in df:
	x.to_excel('USD_rates{}.xlsx'.format(t), sheet_name = 'Sheet1')
	t+=1

