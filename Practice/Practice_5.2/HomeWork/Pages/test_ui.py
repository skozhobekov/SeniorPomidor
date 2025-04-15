from login_page import LoginPage
from products_page import ProductPage
from checkout_page import CheckOutPage
from constants import username
from constants import password
from constants import firstname
from constants import lastname
from constants import postalCode

def test_login(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    login_page.login(username, password)
    login_page.logout()


def test_add_item_to_cart(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    login_page.login(username, password)
    product_page = ProductPage(page)
    product_page.add_first_item_to_cart()

def test_checkout_create(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    product_page = ProductPage(page)
    checkout_page = CheckOutPage(page)
    login_page.login(username, password)
    product_page.add_first_item_to_cart()
    checkout_page.start_checkout()
    checkout_page.fill_checkout_data_and_continue(firstname, lastname, postalCode)
    checkout_page.finish_checkout() #Проверка на отображение нужного нам текста
    login_page.logout()
