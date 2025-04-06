from Base_Page import BasePage
class ProductPage(BasePage):

    FIRST_PRODUCT_SELECTOR = '.inventory_item a:has-text("Sauce Labs Backpack")'
    ADD_TO_CART_FIRST_PRODUCT_SELECTOR = '#add-to-cart'
    GO_TO_CART_BUTTON_SELECTOR = '[data-test="shopping-cart-link"]'
    def __init__(self, page):
        super().__init__(page)
        self.endpoint= "inventory.html"

    def add_first_item_to_cart(self):
        self.wait_for_selector_and_click(self.FIRST_PRODUCT_SELECTOR)
        self.wait_for_selector_and_click(self.ADD_TO_CART_FIRST_PRODUCT_SELECTOR)
        self.wait_for_selector_and_click(self.GO_TO_CART_BUTTON_SELECTOR)


