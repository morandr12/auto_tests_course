"""Модуль содержит тесты MainPage."""

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.pages_links import MAIN_PAGE_LINK


def test_1_guest_should_see_login_link(browser):
    """Тест доступности login_link."""
    link = MAIN_PAGE_LINK
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.should_be_login_link()


def test_2_guest_can_go_to_login_page(browser):
    """Тест перехода на страницу логина."""
    link = MAIN_PAGE_LINK
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    main_page = MainPage(browser=browser, url=link)
    # открываем страницу и переходим на страницу логина
    main_page.open().go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
