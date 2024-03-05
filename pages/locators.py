"""Модуль содержит локаторы страниц."""

from selenium.webdriver.common.by import By


class BasePageLocators:
    """Локаторы BasePage."""

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    """Локаторы MainPage."""

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    """Локаторы LoginPage."""

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_FIELD = (By.CSS_SELECTOR, "input#id_registration-email")
    REGISTER_PASSWORD_FIELD = (By.CSS_SELECTOR, "input#id_registration-password1")
    REGISTER_PASSWORD_ACCEPT_FIELD = (By.CSS_SELECTOR, "input#id_registration-password2")
    BTN_REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "button[name='registration_submit'")


class BasketPageLocators:
    """Локаторы BasketPage."""

    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_FORMSET = (By.CSS_SELECTOR, "#content_inner > #basket_formset")


class ProductPageLocators:
    """Локаторы ProductPage."""

    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ALERT_SUCCESS = (By.CSS_SELECTOR, "div.alert-success")
    ALERT_SUCCESS_TXT = (By.CSS_SELECTOR, "div.alert-success > div.alertinner > strong")
    ALERT_INFO = (By.CSS_SELECTOR, "div.alert-info")
    ALERT_INFO_TXT = (By.CSS_SELECTOR, "div.alert-info > div.alertinner > p > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main > p.price_color")
