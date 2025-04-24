import time
import pytest
import logging
from datetime import datetime
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Create a 'logs' directory if it doesn't exist
log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
os.makedirs(log_dir, exist_ok=True)

# Create a timestamped log file path
log_filename = datetime.now().strftime("test_log_%Y-%m-%d_%H-%M-%S.log")
log_path = os.path.join(log_dir, log_filename)

# Set up logger with file and console handlers
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler(log_path)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('%(message)s'))  # Clean output in console

# Add both handlers
logger.addHandler(file_handler)
logger.addHandler(console_handler)

@pytest.mark.parametrize("url", [
    "https://www.actcorp.in/campaigns/actfibernet-cd4"
])
def test_open_webpage(url):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    try:
        driver.get(url)
        time.sleep(5)
        logger.info("Webpage is available")
    except Exception as e:
        logger.error(f"Failed to open: {url} - Error: {e}")
        raise
    finally:
        driver.quit()
