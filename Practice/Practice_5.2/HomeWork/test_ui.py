from Login_Page import LoginPage
from products_page import ProductPage
from CheckOut_Page import CheckOutPage
from constants import username
from constants import password
from constants import firstname
from constants import lastname
from constants import postalCode

def test_login(browser):
    page = browser.new_page()
    loginPage = LoginPage(page)
    loginPage.login(username, password)
    loginPage.logout()

def test_add_item_to_cart(browser):
    page = browser.new_page()
    loginPage = LoginPage(page)
    loginPage.login(username, password)
    productPage = ProductPage(page)
    productPage.add_first_item_to_cart()

def test_checkout_create(browser):
    page = browser.new_page()
    loginPage = LoginPage(page)
    productPage = ProductPage(page)
    checkOutPage = CheckOutPage(page)
    loginPage.login(username, password)
    productPage.add_first_item_to_cart()
    checkOutPage.start_checkout()
    checkOutPage.fill_the_checkout_data_and_continue(firstname, lastname, postalCode)
    checkOutPage.finish_checkout()
    loginPage.logout()
