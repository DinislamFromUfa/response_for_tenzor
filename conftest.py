import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

@pytest.fixture()
def browser():
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_browser = webdriver.Chrome(options=chrome_options)
    chrome_browser.implicitly_wait(10)
    return chrome_browser