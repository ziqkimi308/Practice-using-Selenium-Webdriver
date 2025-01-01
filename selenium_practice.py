from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Constant
WEBSITE_URL = "https://selenium-practice.netlify.app/"
CHROME_DRIVER_PATH = r""

# In Python, variable names are case-sensitive. So you can use these var names
NAME = "John Wick"
EMAIL = "johnwick@gmail.com"
DATE = "06-11-1990"

# Setup driver
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(WEBSITE_URL)

# Name
name = driver.find_element(By.ID, "name")
name.send_keys(NAME)

# Selection
selection = driver.find_element(By.XPATH, "//*[@id=\"selection\"]/option[2]")
selection.click()

# Checkbox
check2 = driver.find_element(By.NAME, "check2")
check3 = driver.find_element(By.NAME, "check3")
check2.click()
check3.click()

# Date
date = driver.find_element(By.NAME, "date")
date.send_keys(DATE)

# Submit button
submit = driver.find_element(By.XPATH, "/html/body/form/button")
submit.click()

# Last
input("Press ENTER to quit...")
driver.quit()