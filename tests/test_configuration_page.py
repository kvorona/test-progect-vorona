import pytest
from pages.utils import create_driver, User


class TestConfigurationPage:

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
    def user_with_configuration_answer(self, registered_user, authorization_page):
        main_page = authorization_page.sign_in(registered_user.email, registered_user.password)

        configuration = main_page.select_settings()
        configuration.go_to_configuration_add_answer()
        configuration.logout_user_from_conf()
        yield registered_user

    @pytest.fixture(scope="function")
    def authorization_page(self):
        driver = create_driver()
        from pages.authorization_page import AuthorizationPage
        yield AuthorizationPage(driver)
        driver.close()

    def test_add_new_configuration_answer(self, registered_user, authorization_page):
        """
        Pre-condition:
        - Open base page
        - Create test user
        Steps:
        - Authorization with user
        - Go to settings configuration
        - Go to configuration 'ready' answers
        - Add new configuration 'ready' answer
        Check:
        - Verify that new configuration 'ready' answer is present
        """

        main_page = authorization_page.sign_in(registered_user.email, registered_user.password)

        configuration = main_page.select_settings()
        configuration.go_to_configuration_add_answer()
        configuration.verify_new_ready_answer()

    def test_delete_configuration_answer(self, user_with_configuration_answer, authorization_page):
        """
        Pre-condition:
        - Open base page
        - Create test user
        - Create configuration 'ready' answer
        Steps:
        - Authorization with user
        - Go to settings configuration
        - Go to configuration 'ready' answers
        - Delete configuration 'ready' answer
        Check:
        - Verify that 'ready' answer was successfully deleted
        """

        main_page = authorization_page.sign_in(user_with_configuration_answer.email,
                                               user_with_configuration_answer.password)

        configuration = main_page.select_settings()
        configuration.click_on_configuration_ready_answer()
        configuration.delete_configuration_answer()

        configuration.successfully_message_delete()
