from time import sleep

from constants.main_page import MainPageConstants
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constants = MainPageConstants()

    # def click_on_research_field(self, xpath):
    # def go_to_main_page(self):
    #     self.click(self.constants.)

    def search_product(self, text_for_search: str):
        # assert self.click(self.constants.CRAFTA)
        # assert self.click(self.constants.SEARCH_FIELD)
        sleep(1)
        self.fill_field(xpath=self.constants.SEARCH_FIELD, value=text_for_search)
        sleep(1)
        self.click(self.constants.SEARCH_BUTTON_XPATH)
        sleep(1)

    # def add_product_to_trash(self):
    #     self.click(self.constants.BUY_SELECTED_PRODUCT)

    # def verify_message_confirm_mail(self):
    #     self.is_element_exists(self.constants.CONFIRM_EMAIL_MESSAGE)

    def select_ukraine_product(self):
        sleep(2)
        self.find_element(self.constants.PRODUCT_UKRAINE)
        sleep(2)
        self.click(self.constants.BUY_PRODUCT)
