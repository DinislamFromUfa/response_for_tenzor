from pages.contacts_page import ContactsPage


def test_check_region_partners(browser):
    contacts_page = ContactsPage(browser)
    contacts_page.open()
    contacts_page.go_to_contacts_page()
    assert len(contacts_page.check_partner_on_contacts()) > 0 and contacts_page.check_region_on_contacts() == True

def test_switch_to_new_region(browser):
    contacts_page = ContactsPage(browser)
    contacts_page.open()
    contacts_page.go_to_contacts_page()
    current_partners = contacts_page.check_partner_on_contacts()

    data = contacts_page.switch_region_to_kamchatskij_kraj()
    changed_url = data[0]
    changed_title = data[1]
    changed_partners = data[2:]
    assert ("https://saby.ru/contacts/41-kamchatskij-kraj?tab=clients" == changed_url
            and "Камчатский" in changed_title
            and changed_partners != current_partners)

