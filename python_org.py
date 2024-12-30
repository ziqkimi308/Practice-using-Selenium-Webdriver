from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# CONSTANT
CHROME_DRIVER_PATH = r"E:\Applications\chromedriver-win64\chromedriver.exe"
PYTHON_ORG_URL = "https://www.python.org/"

# Setup service and webdriver
service = Service(CHROME_DRIVER_PATH)
drive = webdriver.Chrome(service=service)
drive.get(PYTHON_ORG_URL)

# Specify dates and events
dates = drive.find_elements(By.CSS_SELECTOR, ".event-widget time")
events = drive.find_elements(By.CSS_SELECTOR, ".event-widget .menu a")

# Create dictionary of events and dates
event_dict = {}
for n in range(len(events)):
	event_dict[n] = {
		"time": dates[n].get_attribute("datetime").split("T")[0],
		"name": events[n].text
	}

print(event_dict)

drive.quit()