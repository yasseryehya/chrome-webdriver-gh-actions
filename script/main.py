from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# Initialize Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Your Selenium test code goes here

# Close the WebDriver
driver.quit()
