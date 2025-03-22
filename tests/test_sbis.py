from pages.sbis_page import SbisPage


def test_download_plugin(browser):
    sbis_page = SbisPage(browser)
    sbis_page.open()
    sbis_page.go_to_download_page()
    sbis_page.click_download_button()
    assert '10.43' == str(sbis_page.check_file_size())

