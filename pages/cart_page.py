from constants.cart_page import CartPageConstants
from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constants = CartPageConstants()

    def verify_in_shopping_cart(self):
        self.is_element_exists(self.constants.SHOPPING_CART)

    def verify_can_buy_product(self):
        self.is_element_exists(self.constants.SHOPPING_CART_BUY)

    def verify_can_continue_shopping(self):
        self.is_element_exists(self.constants.CONTINUE_SHOPPING)

    def count_product_in_basket(self):
        count = self.find_element(self.constants.COUNT_IN_BASKET).text_content()
        return int(count)
