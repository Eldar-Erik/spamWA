import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
