"""Модуль содержит PageObject LoginPage"""

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    """Класс PageObject LoginPage"""

    def should_be_login_page(self):
        """Проверка, что это LoginPage."""
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """Проверка url."""
        # реализуйте проверку на корректный url адрес
        assert "login" in self.url

    def should_be_login_form(self):
        """Проверка login_form."""
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        """Проверка register_form."""
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email: str, password: str):
        """Регистрация нового пользователя."""
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_ACCEPT_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BTN_REGISTRATION_SUBMIT).click()
        return self