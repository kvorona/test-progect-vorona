class RegistrationPageConstants:
    SING_UP_XPATH = '//a[@href="https://crafta.ua/uk/auth/register"]'
    FIRST_NAME_FIELD_XPATH = '//input[@name="first_name"]'
    LAST_NAME_FIELD_XPATH = '//input[@name="last_name"]'
    EMAIL_FIELD_XPATH = '//input[@name="email"]'
    PHONE_FIELD_XPATH = '//input[@name="phone"]'
    PASSWORD_FIELD_XPATH = '//input[@name="password"]'
    SING_UP_BUTTON_XPATH = '//button[@type="submit"]'
    ERROR_EMAIL_XPATH = "//div[contains(text(), 'Введіть коректний email')]"
    ERROR_NAME_XPATH = '//div[contains(text(), "Це поле обов")][1]'
    ERROR_LAST_NAME_XPATH = '//div[contains(text(), "Це поле обов")][2]'
    ERROR_PHONE_XPATH = '//div[contains(text(), "Це поле обов")][3]'
    ERROR_PASSWORD_XPATH = '//div[contains(text(), "Це поле обов")][4]'
    ADD_PRODUCT_XPATH = '//a[@data-event-action="Add new product click"]'
    MESSAGE_XPATH = '//a[@class="ek-button ek-button_padding_none ek-button_theme_brand-orange-link"]'
    LIKE_PRODUCT_XPATH = '//a[@class="ek-button ek-button_padding_none ek-button_theme_brand-orange-link ' \
                         'ek-button_weight_medium"]'
    USER_AVATAR_XPATH = '//img[@data-toggle="dropdown"]'
    LOGOUT_XPATH = '//a[@href="https://crafta.ua/uk/auth/logout" and contains(text(), "Вихід")]'
