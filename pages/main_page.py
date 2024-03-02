"""Модуль содержит PageObject MainPage"""
from .base_page import BasePage
# from .login_page import LoginPage
from .locators import MainPageLocators


class MainPage(BasePage):
    """Класс PageObject MainPage"""

    def go_to_login_page(self):
        """Переход на страницу LoginPage"""
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        """Проверка ссылки на страницу LoginPage"""
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
