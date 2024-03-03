"""Модуль содержит PageObject BasePage"""

import math
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from .locators import BasePageLocators


class BasePage:
    """Класс PageObject BasePage"""

    def __init__(self, browser: webdriver, url: str, timeout: int = 10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """Открыть станицу."""
        self.browser.get(self.url)
        return self

    def is_element_present(self, how: str, what: str):
        """Проверка существования локатора элемента."""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how: str, what: str, timeout=4):
        """Проверка отсутствия локатора элемента."""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        """Проверка исчезновения локатора элемента."""
        try:
            WebDriverWait(self.browser, timeout, 1, [TimeoutException]).until_not(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        """Решить вопрос на alert (для Stepik)."""
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def go_to_login_page(self):
        """Переход на страницу LoginPage"""
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        """Проверка ссылки на страницу LoginPage"""
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
