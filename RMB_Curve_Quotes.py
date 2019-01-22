import numpy as np
import pandas as pd
from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\User\chromedriver.exe")
driver.implicitly_wait(30)
driver.get('https://www.rmb.co.za/fixed-income-rates')
df = pd.read_html(driver.find_element_by_id("fixed-income-table").get_attribute('outerHTML'))[0]
np.savetxt("Swap_rates.csv", df, delimiter=",", fmt='%s')

