import pytest

from pages.utils import create_driver


class TestConfigurationPage:


    def test_changes_message_configuration(self):
        driver = create_driver()
        from pages.configuration_page import ConfigurationPage
        configuration = ConfigurationPage(driver)

        from pages.authorization_page import AuthorizationPage
        open_authorization_url = AuthorizationPage(driver)

        open_authorization_url.go_to_authorization_page()
        open_authorization_url.sign_in()

        configuration.go_to_configuration_add_answer()
        configuration.verify_new_ready_answer()
        driver.close()
