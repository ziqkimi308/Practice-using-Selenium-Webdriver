from selenium import webdriver
# Some libraries, like selenium, don’t automatically expose everything in their submodules. You need to import specific submodules or classes directly
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# CONSTANT
CHROME_DRIVER_PATH = r"E:\Applications\chromedriver-win64\chromedriver.exe"
AMAZON_URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

# Setup Chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Optional: Run in headless mode (no UI)
# chrome_options.add_argument("--disable-gpu")  # Optional: Disable GPU for headless
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# Main Code
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(AMAZON_URL)

# Specify price
price = driver.find_element(By.XPATH, "//*[@id=\"corePriceDisplay_desktop_feature_div\"]/div[1]/span[2]")
print(price.text)

# Indicator of code end
print("Done!")

# Last
driver.quit()
