class MainPageConstants:
    SEARCH_FIELD = '//input[@name="search_text"]'
    SEARCH_BUTTON_XPATH = '//button[@type="submit"]'
    PRODUCT_XPATH = '//a[@href="https://crafta.ua/lots/6538685359-prapor-ukrayini"][1]'
    CONFIRM_EMAIL_MESSAGE = '//h1[contains(text(), " Подтвердите свой Email-адрес ")]'
    CRAFTA = '//*[@class="ek-button ek-button_padding_none"]'
    PRODUCT_UKRAINE = '(//*[@class="cft-product-item"])[1]'
    BUY_PRODUCT = '(//*[@class="cft-button__text cft-product-item__buy-button-text"])[1]'
    SALES_BUTTON = '//*[@class="ek-text ek-text_size_small ek-text_weight_medium ek-text_color_brand-orange" and contains(text(), "Знижки")]'
