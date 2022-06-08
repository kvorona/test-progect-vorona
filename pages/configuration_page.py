
from constants.configuration_page import ConfigurationPageConstants
from pages.authorization_page import AuthorizationPage
from pages.base_page import BasePage

TEXT_NAME = 'Some name'
TEXT_MESSAGE = 'Some text message'


class ConfigurationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = ConfigurationPageConstants()
        self.authorization_page = AuthorizationPage(driver)

    def click_on_avatar(self):
        self.click(self.constants.USER_AVATAR_XPATH)

    def click_on_configuration(self):
        self.click(self.constants.CONFIGURATION_XPATH)

    def click_on_configuration_ready_answer(self):
        self.click(self.constants.CONFIGURATION_READY_ANSWER)

    def click_on_save_button(self):
        self.click(self.constants.SAVE_BUTTON_CONFIGURATION)

    def verify_new_ready_answer(self):
        assert self.is_element_exists(self.constants.NEW_READY_ANSWER)

    def add_button_answer(self):
        self.click(self.constants.ADD_ANSWER_BUTTON)

    def fill_body_for_answer(self, text):
        self.fill_field(self.constants.FIELD_TEXT_MESSAGE, text)

    def fill_name_for_answer(self, name):
        self.fill_field(self.constants.FIELD_NAME, name)

    def go_to_configuration_add_answer(self):
        self.click_on_avatar()
        self.click_on_configuration()
        self.click_on_configuration_ready_answer()
        self.add_button_answer()
        self.fill_name_for_answer(TEXT_NAME)
        self.fill_body_for_answer(TEXT_MESSAGE)
        self.click_on_save_button()
