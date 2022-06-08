from constants.cart_page import CartPageConstants
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constants = CartPageConstants()

    def verify_in_shopping_cart(self):
        assert self.is_element_exists(self.constants.SHOPPING_CART)

    def verify_can_buy_product(self):
        assert self.is_element_exists(self.constants.SHOPPING_CART_BUY)

    def verify_can_continue_shopping(self):
        assert self.is_element_exists(self.constants.CONTINUE_SHOPPING)
