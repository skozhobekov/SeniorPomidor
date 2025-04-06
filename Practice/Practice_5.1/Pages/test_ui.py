from pydoc import pager
from Login_Page import LoginPage
from Inventory_Page import InventoryPage
from CheckOut_Page import CheckOutPage
import time
from playwright.sync_api import sync_playwright

def test_func(browser):
    page = browser.new_page()
    loginPage = LoginPage(page)
    inventoryPage = InventoryPage(page)
    checkoutPage = CheckOutPage(page)
    loginPage.login("problem_user", "secret_sauce")
    inventoryPage.add_first_item_to_cart()
    # checkoutPage.start_checkout()
    # checkoutPage.fill_checkout_fields("sanjar", "kojobekov", "1996", 50 )

def test_logout(browser):
    page = browser.new_page()
    loginPage = LoginPage(page)
    loginPage.login("problem_user", "secret_sauce")
    loginPage.logout()










# playwright = sync_playwright().start()
# browser = playwright.chromium.launch(headless=False, slow_mo=50) # задержка перед каждым шагом теста
# page = browser.new_page()
# page.goto("https://www.saucedemo.com/v1/")
#
# page.type(selector='#user-name', text='problem_user', delay=75) #delay - последовательный ввод
# page.fill(selector='#password', value='secret_sauce' )  #password = id, .password = class
# page.click(selector='#login-button')
# page.wait_for_url("https://www.saucedemo.com/v1/inventory.html", timeout=5000) #ожидание конкретной страницы
# page.is_visible(selector="#item_4_title_link") #проверка видимости элемента
# page.is_enabled(selector="#item_4_title_link") #проверка видимости элемента
# #page.click(selector="#item_4_title_link")
# but1 = '.inventory_item a:has-text("Sauce Labs Backpack")' #вложенный селектор
# page.click(but1)
# page.get_by_text('ADD TO CART').click()
# shoping_card = '#shopping_cart_container'
# page.click(shoping_card)
# time.sleep(5) #пауза
# browser.close()
# playwright.stop()




