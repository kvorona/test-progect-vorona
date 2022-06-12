class MainPageConstants:
    PRODUCT_XPATH = '//a[@href="https://crafta.ua/lots/6538685359-prapor-ukrayini"][1]'
    PRODUCT_UKRAINE = '(//*[@class="cft-product-item"])[1]'
    BUY_PRODUCT = '(//*[@class="cft-button__text cft-product-item__buy-button-text"])[1]'
    SALES_BUTTON = '//*[@class="ek-text ek-text_size_small ek-text_weight_medium ek-text_color_brand-orange" ' \
                   'and contains(text(), "Знижки")]'
    USER_AVATAR_XPATH = '//img[@data-toggle="dropdown"]'
    CONFIGURATION_XPATH = '(//*[contains(text(), "Налаштування")])[1]'
