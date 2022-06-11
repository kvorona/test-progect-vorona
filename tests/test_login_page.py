import pytest
from pages.utils import User, create_driver


class TestRegistrationPage:

    @pytest.fixture(scope="function")
    def random_user(self):
        return User()

    @pytest.fixture(scope="function")
    def open_base_url(self):
        driver = create_driver()
        from pages.registration_page import RegistrationPage
        yield RegistrationPage(driver)
        driver.close()

    @pytest.fixture(scope="function")
    def open_authorization_url(self):
        driver = create_driver()
        from pages.authorization_page import AuthorizationPage
        yield AuthorizationPage(driver)
        driver.close()

    @pytest.fixture(scope="function")
    def registered_user(self, open_base_url, random_user):
        open_base_url.registered_user(random_user)
        open_base_url.logout_user()
        return random_user

    # @pytest.fixture(scope="function")
    # def logout(self, open_base_url):
    #     yield
    #     open_base_url.logout_user()

    def test_registration_with_empty_field(self, open_base_url):
        """
        Pre-condition:
        - Create driver
        - Open base page
        Steps:
        - Go to registration page
        - Fill empty field name
        - Fill empty field surname
        - Fill empty field email
        - Fill empty field phone
        - Fill empty field password
        - Clear "Sign up"
        Check:
        - Verify error message
        After test:
        - Close site
        """
        open_base_url.go_to_registration_page()
        open_base_url.empty_field_for_registration_form()
        open_base_url.verify_error_message_sign_up()

    def test_registration(self, open_base_url, random_user):
        """
        Pre-condition:
        - Create driver
        - Open base page
        Steps:
        - Go to registration page
        - Fill field name
        - Fill field surname
        - Fill field email
        - Fill field phone
        - Fill field password
        - Click "Sign up"
        Check:
        - Verify successfully registration
        After test:
        - Close site
        """
        open_base_url.go_to_registration_page()
        open_base_url.fill_field_for_registration_form(random_user)
        open_base_url.click_on_sign_up_button()
        open_base_url.successful_message_sign_up()

    def test_authorization_with_correct_value(self, open_authorization_url, registered_user):
        """
        Pre-condition:
        - Create driver
        - Create random user and logout
        - Open base page
        Steps:
        - Go to authorization page
        - Fill field email
        - Fill field password
        - Click "Sign in"
        Check:
        - Verify successfully sign in
        After test:
        - Close site
        """
        open_authorization_url.sign_in(registered_user.email, registered_user.password)
        open_authorization_url.successful_message_sign_in()
