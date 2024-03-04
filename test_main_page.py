"""Модуль содержит тесты MainPage."""

import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.pages_links import MAIN_PAGE_LINK


@pytest.mark.login_guest
class TestLoginFromMainPage:
    """Класс тестов логина с основой страницы. """
    def test_guest_should_see_login_link(self, browser):
        """Тест доступности login_link."""
        link = MAIN_PAGE_LINK
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        """Тест перехода на страницу логина."""
        link = MAIN_PAGE_LINK
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        main_page = MainPage(browser, link)
        # открываем страницу и переходим на страницу логина
        main_page.open().go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """Тест перехода на страницу пустой корзины."""
    link = MAIN_PAGE_LINK
    main_page = MainPage(browser, link)
    main_page.open().go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_basket_formset().should_be_empty_basket_message()
