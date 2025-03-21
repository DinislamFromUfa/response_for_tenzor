from pages.contacts_page import ContactsPage
from pages.tenzor_page import TenzorPage


def test_exist_text_and_about(browser):
    contacts_page = ContactsPage(browser)
    contacts_page.open()
    contacts_page.go_to_contacts_page()
    contacts_page.go_to_tenzor_page()

    tenzor_page = TenzorPage(browser)
    expected_text = "Сила в людях"
    actual_text = tenzor_page.check_text_in_block()
    assert expected_text == actual_text

def test_height_and_width(browser):
    contacts_page = ContactsPage(browser)
    contacts_page.open()
    contacts_page.go_to_contacts_page()
    contacts_page.go_to_tenzor_page()
    tenzor_page = TenzorPage(browser)
    tenzor_page.go_to_about_page()
    assert "Все изображения имеют одинаковые размеры" == tenzor_page.check_width_and_height_of_photos()

