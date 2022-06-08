from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(driver=driver, timeout=5)

    def click(self, xpath):
        self.driver.find_element(by=By.XPATH, value=xpath).click()

    def fill_field(self, xpath, value):
        field = self.driver.find_element(by=By.XPATH, value=xpath)
        field.clear()
        field.send_keys(value)

    def fill_field_strokes(self, xpath, value):
        field = self.driver.find_element(by=By.XPATH, value=xpath)
        field.clear()

        is_first_symbol = True
        for digit in value:
            field.send_keys(digit)
            if is_first_symbol:
                field.send_keys(Keys.ARROW_RIGHT)
                is_first_symbol = False

    def find_element(self, xpath):
        self.driver.find_element(by=By.XPATH, value=xpath)

    def is_element_exists(self, xpath):
        try:
            self.driver.find_element(by=By.XPATH, value=xpath)
            return True
        except (TimeoutError, NoSuchElementException):
            return False

