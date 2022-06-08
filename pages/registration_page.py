from time import sleep

from constants.registration_page import RegistrationPageConstants
from pages.base_page import BasePage


class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = RegistrationPageConstants()

    def click_on_sign_up_button(self):
        self.click(self.constants.SING_UP_BUTTON_XPATH)

    def empty_field_for_registration_form(self, first_name='', last_name='', email='', phone='', password=''):
        self.fill_field(xpath=self.constants.FIRST_NAME_FIELD_XPATH, value=first_name)
        self.fill_field(xpath=self.constants.LAST_NAME_FIELD_XPATH, value=last_name)
        self.fill_field(xpath=self.constants.EMAIL_FIELD_XPATH, value=email)
        self.fill_field(xpath=self.constants.PHONE_FIELD_XPATH, value=phone)
        self.fill_field(xpath=self.constants.PASSWORD_FIELD_XPATH, value=password)
        self.click(self.constants.SING_UP_BUTTON_XPATH)

    def fill_field_for_registration_form(self, user):
        self.fill_field(xpath=self.constants.FIRST_NAME_FIELD_XPATH, value=user.first_name)
        self.fill_field(xpath=self.constants.LAST_NAME_FIELD_XPATH, value=user.last_name)
        self.fill_field(xpath=self.constants.EMAIL_FIELD_XPATH, value=user.email)
        self.fill_field_strokes(xpath=self.constants.PHONE_FIELD_XPATH, value=user.phone)
        self.fill_field(xpath=self.constants.PASSWORD_FIELD_XPATH, value=user.password)
        self.click(self.constants.SING_UP_BUTTON_XPATH)

    def verify_error_message_sign_up(self):
        assert self.is_element_exists(self.constants.EMAIL_FIELD_XPATH)
        assert self.is_element_exists(self.constants.ERROR_PASSWORD_XPATH)
        assert self.is_element_exists(self.constants.ERROR_EMAIL_XPATH)
        assert self.is_element_exists(self.constants.ERROR_PHONE_XPATH)
        assert self.is_element_exists(self.constants.ERROR_LAST_NAME_XPATH)

    def successful_message_sign_up(self):
        assert self.is_element_exists(self.constants.ADD_PRODUCT_XPATH)
        assert self.is_element_exists(self.constants.MESSAGE_XPATH)
        assert self.is_element_exists(self.constants.LIKE_PRODUCT_XPATH)
        assert self.is_element_exists(self.constants.USER_AVATAR_XPATH)

    def logout_user(self):
        self.click(self.constants.USER_AVATAR_XPATH)
        self.click(self.constants.LOGOUT_XPATH)

    def go_to_registration_page(self):
        self.click(self.constants.SING_UP_XPATH)
