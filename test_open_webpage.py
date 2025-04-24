import time
import pytest
import logging
from datetime import datetime
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
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

# Avoid duplicate handlers when running multiple times
if not logger.handlers:
    # File handler
    file_handler = logging.FileHandler(log_path)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter('%(message)s'))
    logger.addHandler(console_handler)

@pytest.mark.parametrize("url", [
    "https://www.actcorp.in/campaigns/actfibernet-cd4"
])
def test_open_webpage(url):
    # Set up Chrome options for headless mode (CI-compatible)
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    try:
        logger.info(f"Opening URL: {url}")
        driver.get(url)
        time.sleep(5)
        assert "ACT" in driver.title or "actcorp" in driver.current_url.lower(), "Page title or URL did not load as expected."
        logger.info("✅ Webpage is available and loaded successfully.")
    except Exception as e:
        logger.error(f"❌ Failed to open: {url} - Error: {e}")
        raise
    finally:
        driver.quit()
        logger.info("🔄 Browser closed.\n")
