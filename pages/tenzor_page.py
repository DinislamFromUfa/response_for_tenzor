from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage




class TenzorPage(BasePage):

    PAGE_URL = 'https://www.tenzor.ru'
    TEXT_POWER_IN_PEOPLE = (By.XPATH, '//p[contains(text(), "Сила")]')
    ABOUT_LINK = (By.XPATH, '//a[@href="/about" and contains(text(), "Подробнее")]')
    IMAGES = (By.XPATH, '//*[@class="tensor_ru-container tensor_ru-section tensor_ru-About__block3"]/descendant::img')

    def __init__(self, browser):
        self.browser = browser
        super().__init__(browser)

    def check_text_in_block(self):
        try:
            print(self.browser.current_url)
            element = self.browser.find_element(*self.TEXT_POWER_IN_PEOPLE)
            return element.text
        except NoSuchElementException:
            print("Элемент с текстом 'Сила в людях' не найден на странице.")
        except Exception as e:
            print(f"Ошибка при поиске текста: {e}")
            return None

    def go_to_about_page(self):
        self.click_with_wait(self.ABOUT_LINK)


    def check_width_and_height_of_photos(self):
        print(self.browser.current_url)
        sizes = []
        images = WebDriverWait(self.browser, 20).until(
            EC.presence_of_all_elements_located(self.IMAGES)
        )
        for image in images:
            width = image.get_attribute('width')
            height = image.get_attribute('height')
            sizes.append((width, height))

        first_size = sizes[0]
        all_sizes_equal = all(size == first_size for size in sizes)

        if all_sizes_equal:
            return "Все изображения имеют одинаковые размеры"
        else:
            return "Размеры различаются"