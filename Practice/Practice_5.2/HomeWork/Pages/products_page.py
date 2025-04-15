from base_page import BasePage
class ProductPage(BasePage):

    FIRST_PRODUCT_SELECTOR = '.inventory_item a:has-text("Sauce Labs Backpack")'
    ADD_TO_CART_FIRST_PRODUCT_SELECTOR = '#add-to-cart'
    REMOVE_FROM_CART_SELECTOR = '#remove'
    GO_TO_CART_BUTTON_SELECTOR = '[data-test="shopping-cart-link"]'
    CART_PAGE_SELECTOR = '[data-test="title"]'

    def __init__(self, page):
        super().__init__(page)
        self.endpoint= "inventory.html"

    def add_first_item_to_cart(self):
        self.wait_for_selector_and_click(self.FIRST_PRODUCT_SELECTOR)
        self.assert_text_in_element(self.ADD_TO_CART_FIRST_PRODUCT_SELECTOR, "Add to cart")
        self.wait_for_selector_and_click(self.ADD_TO_CART_FIRST_PRODUCT_SELECTOR)
        self.assert_text_in_element(self.REMOVE_FROM_CART_SELECTOR, "Remove")
        self.wait_for_selector_and_click(self.GO_TO_CART_BUTTON_SELECTOR)
        self.assert_text_in_element(self.CART_PAGE_SELECTOR, "Your Cart")


