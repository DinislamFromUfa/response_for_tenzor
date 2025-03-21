from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ContactsPage(BasePage):


    PAGE_URL = "https://www.sbis.ru"

    CONTACTS_BUTTON = (By.XPATH, '//div[text()="Контакты"]')
    LINK_CONTACTS = (By.XPATH, '//a[@href="/contacts"]/child::span')
    TENZOR_LINK = (By.XPATH, '//a[@class="sbisru-Contacts__logo-tensor mb-12"]/child::img')

    def __init__(self, browser):
        self.browser = browser
        super().__init__(browser)


    def go_to_contacts_page(self):
        self.click_with_wait(self.CONTACTS_BUTTON)
        self.click_with_wait(self.LINK_CONTACTS)


    def go_to_tenzor_page(self):
        initial_number_of_windows = len(self.browser.window_handles)

        self.click_with_wait(self.TENZOR_LINK)

        WebDriverWait(self.browser, 20).until(
            EC.number_of_windows_to_be(initial_number_of_windows + 1)
        )

        all_windows = self.browser.window_handles

        self.browser.switch_to.window(all_windows[-1])


