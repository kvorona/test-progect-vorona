import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from constants.base import BaseConstants

from pages.utils import User


# text_for_search = 'ПРАПОР УКРАЇНИ'


class TestMainPage:

    @pytest.fixture(scope="function")
    def open_base_url(self):
        driver = WebDriver(executable_path=BaseConstants.DRIVER_PATH)
        driver.implicitly_wait(1)
        driver.get(BaseConstants.BASE_URL)
        from pages.registration_page import RegistrationPage
        yield RegistrationPage(driver)
        driver.close()

    @pytest.fixture(scope="function")
    def open_main_url(self):
        driver = WebDriver(executable_path=BaseConstants.DRIVER_PATH)
        driver.implicitly_wait(1)
        driver.get(BaseConstants.BASE_URL)
        from pages.main_page import MainPage
        yield MainPage(driver)
        driver.close()

    @pytest.fixture(scope="function")
    def random_user(self):
        return User()

    # @pytest.fixture(scope="function")
    # def register_user(self, open_base_url, random_user):
    #     open_base_url.fill_field_for_registration_form(random_user)
    #     open_base_url.click_on_sign_up_button()
    #     yield
    #     open_base_url.logout_user()
    #     return random_user

    @pytest.fixture(scope="function")
    def register_user(self, open_base_url, random_user):
        open_base_url.go_to_registration_page()
        open_base_url.fill_field_for_registration_form(random_user)
        open_base_url.click_on_sign_up_button()
        # open_base_url.logout_user()
        # return random_user

        # open_base_url.click_on_sign_up_button()
        # yield
        # open_base_url.logout_user()
        # return random_user

    # open_base_url.go_to_registration_page()
    # open_base_url.fill_field_for_registration_form(random_user)
    # open_base_url.click_on_sign_up_button()
    # open_base_url.logout_user()
    # return random_user

    def test_find_product(self, open_main_url, register_user):
        """
                Pre-condition:
                - Create driver
                - Open base page
                - Create test user
                Steps:
                - Open base page
                - Input search text
                - Find product
                - Open product
                - Click buy
                Check:
                - Verify that product in trash
                - Verify that button "Buy" presented
                - Verify that button "Continue shopping" presented
                - Check count in basket
                After test:
                - Close site
                """

        open_main_url.search_product('ПРАПОР УКРАЇНИ')
        open_main_url.select_ukraine_product()

        from pages.cart_page import CartPage
        cart_page = CartPage(self.driver)

        assert cart_page.count_product_in_basket() == 1

        assert cart_page.verify_in_shopping_cart()
        assert cart_page.verify_can_buy_product()
        assert cart_page.verify_can_continue_shopping()
