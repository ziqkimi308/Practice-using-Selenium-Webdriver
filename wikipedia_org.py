from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# CONSTANT
WEBSITE_URL = "https://en.wikipedia.org/wiki/Main_Page"
CHROME_DRIVER_PATH = r""

# Setup webdriver
service = Service(CHROME_DRIVER_PATH)
drive = webdriver.Chrome(service=service)
# Maximise browser window size
drive.maximize_window()
drive.get(WEBSITE_URL)

# Specify articles number
# article_number = drive.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(article_number.text)
# print("Process done!")

# Click Wikipedia link
# wikipedia_article = drive.find_element(By.CSS_SELECTOR, "#Welcome_to_Wikipedia a")
# wikipedia_article.click()
# print("Process done!")

# Writing into placeholder
placeholder = drive.find_element(By.NAME, "search")
placeholder.send_keys("Python")
placeholder.send_keys(Keys.ENTER)
print("Can send keys.")

input("Press ENTER to close the browser...")

# Last
drive.quit()