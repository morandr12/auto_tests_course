from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_1_guest_should_see_login_link(browser):
    """Проверка доступности login_link."""
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.should_be_login_link()


def test_2_guest_can_go_to_login_page(browser):
    """Проверка перехода на страницу логина"""
    link = "http://selenium1py.pythonanywhere.com/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    main_page = MainPage(browser=browser, url=link)
    # открываем страницу и переходим на страницу логина
    main_page.open().go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
