import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def browser():
    chrome_options = ChromeOptions()
    #chrome_options.add_argument('--headless')
    prefs = {
        "download.default_directory": f"{os.getcwd()}\downloads",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": False,
    }
    chrome_options.add_experimental_option("prefs", prefs)

    service = Service(executable_path=ChromeDriverManager().install())
    chrome_browser = webdriver.Chrome(options=chrome_options, service=service)
    chrome_browser.implicitly_wait(10)
    return chrome_browser