import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from custom_urlgen import *
from selenium.webdriver.chrome.service import Service
from clean import *

# List of URLs to capture screenshots
'''urls = [
    "https://majestic.com/reports/majestic-million",
    "https://google.com",
    "https://www.quantcast.com/",
]
'''
urls = nonphishy_urls

urls = ["https://" + url for url in urls]
print(urls[:5])

# Directory to save the screenshots
screenshot_dir = "screenshots"
os.makedirs(screenshot_dir, exist_ok=True)

# Configure the Chrome WebDriver with options
# service = Service(executable_path=r'/Users/kayle/Projects/Python/helloworld/chromedriver')
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Safari()
driver.maximize_window()
# ...

'''
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)
'''

# Loop through the URLs and capture screenshots
for index, url in enumerate(urls):
    try:
        # Visit the URL
        driver.get(url)
        time.sleep(5)
        #driver.maximize_window()

        # Capture a screenshot and save it with a meaningful name
        screenshot_filename = os.path.join(screenshot_dir, f"screenshot_{index + 600}.png")
        driver.save_screenshot(screenshot_filename)

        print(f"Screenshot saved: {screenshot_filename}")

    except Exception as e:
        print(f"Error capturing screenshot for {url}: {e}")

# Quit the WebDriver
driver.quit()
