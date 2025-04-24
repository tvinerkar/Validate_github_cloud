import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.mark.parametrize("url", [
    "https://www.actcorp.in/campaigns/actfibernet-cd4"  # Replace with your desired URL
])
def test_open_webpage(url):
    # Set up the Chrome WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    try:
        driver.get(url)
        time.sleep(5)  # Wait for 5 seconds
        print("Webpage is available")
    finally:
        driver.quit()  # Close the browser
