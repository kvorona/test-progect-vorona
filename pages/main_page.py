from time import sleep
from selenium.webdriver import ActionChains

from constants.main_page import MainPageConstants
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = MainPageConstants()

    def select_ukraine_product(self):
        self.click(self.constants.SALES_BUTTON)
        self.driver.execute_script("window.scrollTo(0,600)")
        sleep(2)
        a = ActionChains(self.driver)
        m = self.driver.find_element_by_xpath(self.constants.PRODUCT_UKRAINE)
        a.move_to_element(m).perform()
        self.wait_until_displayed(self.constants.BUY_PRODUCT)
        self.click(self.constants.BUY_PRODUCT)
        from pages.cart_page import CartPage
        return CartPage(self.driver)

    def click_on_avatar(self):
        self.click(self.constants.USER_AVATAR_XPATH)

    def click_on_configuration(self):
        self.click(self.constants.CONFIGURATION_XPATH)

    def select_settings(self):
        self.click_on_avatar()
        self.click_on_configuration()
        from pages.configuration_page import ConfigurationPage
        return ConfigurationPage(self.driver)
