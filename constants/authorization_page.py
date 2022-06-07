class AuthorizationPageConstants:
    SING_IN_XPATH = "//span[@class='ek-text ek-text_color_brand-orange ek-text_weight_medium ek-text_size_default' and " \
                    "contains(text(), 'Вхід')]"
    SIGN_IN_EMAIL_XPATH = '//input[@type="text" and @name="username"]'
    SIGN_IN_PASSWORD_XPATH = '//input[@type="password" and @name="password"]'
    SIGN_IN_BUTTON_XPATH = '//button[@type="submit"]'
    USER_AVATAR_XPATH = '//img[@data-toggle="dropdown"]'
    FORGOT_PASSWORD_XPATH = '//a[@href="https://crafta.ua/uk/auth/password/reset"]'
    SIGN_UP_FROM_SING_IN_PAGE = './/a[@href="https://crafta.ua/uk/auth/register?next=https://crafta.ua/uk/"' \
                                ' and contains(text(), "Зарегистрироваться")]'
