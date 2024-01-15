from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# Initialize Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Open a website (e.g., Google)
driver.get("https://www.google.com")

# Perform a simple action (e.g., search for "GitHub Actions")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("GitHub Actions")
search_box.submit()

# Wait for the search results page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "search")))

# Verify that the search results contain the expected text
expected_text = "GitHub Actions"
assert (
    expected_text in driver.page_source
), f"Expected text '{expected_text}' not found in page source"

# Close the WebDriver
driver.quit()
