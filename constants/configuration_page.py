class ConfigurationPageConstants:
    USER_AVATAR_XPATH = '//img[@data-toggle="dropdown"]'
    CONFIGURATION_XPATH = '(//*[contains(text(), "Налаштування")])[1]'
    CONFIGURATION_READY_ANSWER = '(//*[contains(text(), "Готові відповіді")])[1]'
    SAVE_BUTTON_CONFIGURATION = '//*[@class="cft-button__text"]'
    MESSAGE_SUCCESSFULLY_SAVE = '//*[@class="cft-flash-message__content"]'
    ADD_ANSWER_BUTTON = '//*[contains(text(), "Додати відповідь")]'
    FIELD_NAME = '//*[@class="cft-input__field" and @name="title"]'
    FIELD_TEXT_MESSAGE = '//*[@class="cft-input__field" and @name="text"]'
    NEW_READY_ANSWER = '//*[@class="cft-template-actions__item cft-template-actions__item_type_name"]'