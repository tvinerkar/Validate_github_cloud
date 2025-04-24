import time
import pytest
import logging
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Setup logging with current date and time in the filename
log_filename = datetime.now().strftime("test_log_%Y-%m-%d_%H-%M-%S.log")
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@pytest.mark.parametrize("url", [
    "https://www.actcorp.in/campaigns/actfibernet-cd4"
])
def test_open_webpage(url):
    # Set up the Chrome WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    try:
        driver.get(url)
        time.sleep(5)  # Wait for 5 seconds
        logging.info(f"Successfully opened: {url}")
        print("Webpage is available")
    except Exception as e:
        logging.error(f"Failed to open: {url} - Error: {e}")
        raise
    finally:
        driver.quit()  # Close the browser
