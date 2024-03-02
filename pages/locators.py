from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ALERT_SUCCESS = (By.CSS_SELECTOR, "div.alert-success")
    ALERT_SUCCESS_TXT = (By.CSS_SELECTOR, "div.alert-success > div.alertinner > strong")
    ALERT_INFO = (By.CSS_SELECTOR, "div.alert-info")
    ALERT_INFO_TXT = (By.CSS_SELECTOR, "div.alert-info > div.alertinner > p > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main > p.price_color")
