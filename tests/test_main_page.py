import pytest
from pages.utils import create_driver, User


class TestMainPage:

    @pytest.fixture(scope="function")
    def random_user(self):
        return User()

    @pytest.fixture(scope="function")
    def registered_user(self, random_user):
        driver = create_driver()
        from pages.registration_page import RegistrationPage
        register_page = RegistrationPage(driver)

        register_page.registered_user(random_user)
        register_page.logout_user()
        yield random_user
        driver.close()

    @pytest.fixture(scope="function")
    def authorization_page(self):
        driver = create_driver()
        from pages.authorization_page import AuthorizationPage
        yield AuthorizationPage(driver)
        driver.close()

    def test_buy_product(self, registered_user, authorization_page):
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
        main_page = authorization_page.sign_in(registered_user.email, registered_user.password)

        cart_page = main_page.select_ukraine_product()

        cart_page.verify_in_shopping_cart()
        cart_page.verify_can_buy_product()
        cart_page.verify_can_continue_shopping()
