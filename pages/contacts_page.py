from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ContactsPage(BasePage):


    PAGE_URL = "https://www.sbis.ru"

    CONTACTS_BUTTON = (By.XPATH, '//div[text()="Контакты"]')
    LINK_CONTACTS = (By.XPATH, '//a[@href="/contacts"]/child::span')
    TENZOR_LINK = (By.XPATH, '//a[@class="sbisru-Contacts__logo-tensor mb-12"]/child::img')

    LINK_REGION = (By.XPATH, '//span[@class="sbis_ru-Region-Chooser ml-16 ml-xm-0"]/child::span')
    LINKS_OF_PARTNERS = (By.XPATH, '//div[@name="itemsContainer"]/child::div')

    LINK_OF_KAMCHATSKIJ_KRAJ = (By.XPATH, '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span/span')

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


    def check_region_on_contacts(self):
        name_of_region = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.LINK_REGION)
        )
        return name_of_region.is_displayed()


    def check_partner_on_contacts(self):
        print(self.browser.current_url)
        partners = []
        try:
            name_of_partners = WebDriverWait(self.browser, 10).until(
                EC.presence_of_all_elements_located(self.LINKS_OF_PARTNERS)
            )

            for name_of_partner in name_of_partners:
                partners.append(name_of_partner)

            return partners
        except Exception as e:
            print(f'Exception on "check_partners": {e}')


    def switch_region_to_kamchatskij_kraj(self):
        changed_values = []

        self.click_with_wait(self.LINK_REGION)
        self.click_with_wait(self.LINK_OF_KAMCHATSKIJ_KRAJ)
        WebDriverWait(self.browser, 15).until(
            EC.url_contains("41-kamchatskij-kraj?tab=clients")
        )

        changed_values.append(self.browser.current_url)
        changed_values.append(self.browser.title)
        changed_values.append(self.LINKS_OF_PARTNERS)

        return changed_values




