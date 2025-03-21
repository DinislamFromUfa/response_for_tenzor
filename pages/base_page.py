from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():

    def __init__(self, browser):
        self.browser:WebDriver = browser


    def open(self):
        self.browser.get(self.PAGE_URL)


    def click_with_wait(self, locator, timeout=10):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located(locator)
            )
            WebDriverWait(self.browser, timeout).until(
                EC.element_to_be_clickable(locator)
            ).click()
        except Exception as e:
            print(f"Exception on 'click_with_wait': {e}")

