from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    ITEM_NAME_IN_ADDED_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) .alertinner > strong")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ITEM_PRICE_IN_ADDED_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(3) .alertinner strong")
