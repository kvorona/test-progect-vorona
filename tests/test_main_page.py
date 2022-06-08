import pytest
from pages.utils import create_driver, User


class TestMainPage:

    @pytest.fixture(scope="function")
    def random_user(self):
        return User()

    @pytest.fixture(scope="function")
    def register_user(self, random_user):
        driver = create_driver()
        from pages.registration_page import RegistrationPage
        registr_page = RegistrationPage(driver)

        registr_page.go_to_registration_page()
        registr_page.fill_field_for_registration_form(random_user)
        registr_page.click_on_sign_up_button()
        registr_page.logout_user()
        return random_user

    def test_buy_product(self, register_user):
        """
                Pre-condition:
                - Open base page
                - Create test user
                Steps:
                - Open base page
                - Select "sales"
                - Click on buy product
                Check:
                - Verify that product in trash
                - Verify that button "Buy" presented
                - Verify that button "Continue shopping" presented
                """
        driver = create_driver()

        from pages.main_page import MainPage
        from pages.authorization_page import AuthorizationPage
        from pages.cart_page import CartPage
        open_authorization_url = AuthorizationPage(driver)
        open_main_url = MainPage(driver)
        cart_page = CartPage(driver)

        open_authorization_url.go_to_authorization_page()
        open_authorization_url.sign_in(register_user.email, register_user.password)

        open_main_url.click_on_sale_button()
        open_main_url.select_ukraine_product()

        cart_page.verify_in_shopping_cart()
        cart_page.verify_can_buy_product()
        cart_page.verify_can_continue_shopping()

        driver.close()
