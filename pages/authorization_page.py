from constants.authorization_page import AuthorizationPageConstants
from pages.base_page import BasePage


class AuthorizationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = AuthorizationPageConstants()

    def sign_in(self, email='email739358@email.com', password='Password550121'):
        self.click(self.constants.SING_IN_XPATH)
        self.fill_field(xpath=self.constants.SIGN_IN_EMAIL_XPATH, value=email)
        self.fill_field(xpath=self.constants.SIGN_IN_PASSWORD_XPATH, value=password)
        self.click(self.constants.SIGN_IN_BUTTON_XPATH)
        from pages.main_page import MainPage
        return MainPage(self.driver)

    def successful_message_sign_in(self):
        assert self.is_element_exists(self.constants.USER_AVATAR_XPATH)
