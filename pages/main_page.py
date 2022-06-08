from time import sleep

from selenium.webdriver import ActionChains

from constants.main_page import MainPageConstants
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constants = MainPageConstants()

    def click_on_sale_button(self):
        self.click(self.constants.SALES_BUTTON)

    def select_ukraine_product(self):
        self.driver.execute_script("window.scrollTo(0,600)")
        sleep(2)
        a = ActionChains(self.driver)
        m = self.driver.find_element_by_xpath(self.constants.PRODUCT_UKRAINE)
        a.move_to_element(m).perform()

        self.click(self.constants.BUY_PRODUCT)
