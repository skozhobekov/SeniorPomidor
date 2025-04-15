from base_page import BasePage

class CheckOutPage(BasePage):
    CHECKOUT_BUTTON_SELECTOR = '[data-test="checkout"]'
    FIRSTNAME_FIELD = '#first-name'
    LASTNAME_FIELD = '#last-name'
    POSTALCODE_FIELD = '#postal-code'
    CONTINUE_BUTTON = '#continue'
    FINISH_BUTTON = '#finish'
    COMPLETED_SELECTOR = '[data-test="complete-header"]'

    def __init__(self, page):
        super().__init__(page)
        self.endpoint = 'checkout-step-one.html'


    def start_checkout(self):
        self.assert_text_in_element(self.CHECKOUT_BUTTON_SELECTOR)
        self.wait_for_selector_and_click(self.CHECKOUT_BUTTON_SELECTOR)
        self.assert_text_presents_on_page("Checkout: Your Information")

    def fill_checkout_data_and_continue(self, firstname, lastname, postal_code):
        self.assert_element_isVisible(self.FIRSTNAME_FIELD)
        self.wait_for_selector_and_type(self.FIRSTNAME_FIELD, firstname)
        self.wait_for_selector_and_type(self.LASTNAME_FIELD, lastname)
        self.wait_for_selector_and_type(self.POSTALCODE_FIELD, postal_code)
        self.wait_for_selector_and_click(self.CONTINUE_BUTTON)

    def finish_checkout(self):
        self.wait_for_selector_and_click(self.FINISH_BUTTON)
        self.assert_text_in_element(self.COMPLETED_SELECTOR, "Thank you for your order!")
