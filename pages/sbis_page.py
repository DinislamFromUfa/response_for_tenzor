import os
from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SbisPage(BasePage):

    PAGE_URL = "https://www.sbis.ru"
    PAGE_OF_DOWNLOADS_URL = (By.LINK_TEXT, "Скачать локальные версии")
    DOWNLOAD_LINK = (By.XPATH, "//a[@href='https://update.saby.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe']")

    FILE_NAME = f'{os.getcwd()}/downloads/sbisplugin-setup-web.exe'

    def __init__(self, browser):
        self.browser = browser
        super().__init__(browser)

    def go_to_download_page(self):
        self.click_with_wait(self.PAGE_OF_DOWNLOADS_URL)

    def click_download_button(self):
        sleep(3)
        self.click_with_wait(self.DOWNLOAD_LINK)
        sleep(10)

    def check_file_size(self):
        file_path = self.FILE_NAME
        if file_path is None:
            return "File not found"
        else:
            size_of_file = os.path.getsize(file_path)/(1024*1024)
        return round(size_of_file, 2)

