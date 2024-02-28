from .pages.main_page import MainPage


def test_1_guest_should_see_login_link(browser):
    """Проверка доступности login_link."""
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_2_guest_can_go_to_login_page(browser):
    """Проверка перехода на страницу логина"""
    link = "http://selenium1py.pythonanywhere.com/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = MainPage(browser=browser, url=link)
    # открываем страницу и переходим на страницу логина
    page.open().go_to_login_page()



