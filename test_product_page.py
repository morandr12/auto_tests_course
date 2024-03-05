"""Модуль содержит тесты ProductPage."""

import time
import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.pages_links import (
    PRODUCTS_PAGE_LINK_1,
    PRODUCTS_PAGE_LINK_2,
    PRODUCTS_PAGE_NEW_YEAR_PROMO_LINKS,
    PRODUCTS_PAGE_PROMO_LINKS,
    LOGIN_PAGE_LINK,
)


class TestUserAddToBasketFromProductPage:
    """Класс с тестами взаимодействия авторизованного юзера с корзиной."""

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """Фикстура регистрации нового пользователя. Возвращает экземпляр браузера."""
        link = LOGIN_PAGE_LINK
        login_page = LoginPage(browser, link)
        login_page.open().register_new_user(
            email=f"{time.time()}@fakeemail.org", password=f"qwerty@{time.time()}"
        )
        login_page.should_be_authorized_user()
        return browser

    @pytest.mark.negative
    def test_user_cant_see_success_message(self, setup):
        """
        Тест отсутствия сообщений о добавленном товаре при открытии страницы продукта.
        Без добавления продукта в корзину.
        """
        link = PRODUCTS_PAGE_LINK_2
        product_page = ProductPage(browser=setup, url=link)
        product_page.open()
        product_page.should_be_alert_success()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, setup):
        """Тест добавления товара в корзину."""
        link = PRODUCTS_PAGE_LINK_2
        product_page = ProductPage(browser=setup, url=link)
        product_page.open().add_product_to_basket()
        product_page.check_product_added_to_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    """Тест наличия ссылки на LoginPage"""
    link = PRODUCTS_PAGE_LINK_2
    product_page = ProductPage(browser, link)
    product_page.open().should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    """Тест перехода на страницу логина."""
    link = PRODUCTS_PAGE_LINK_2
    product_page = ProductPage(browser, link)
    product_page.open().go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
@pytest.mark.negative
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """Тест отсутствия товаров в корзине при переходе на страницу корзины"""
    link = PRODUCTS_PAGE_LINK_1
    product_page = ProductPage(browser, link)
    product_page.open().go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_basket_formset().should_be_empty_basket_message()


@pytest.mark.need_review
@pytest.mark.parametrize("link", PRODUCTS_PAGE_NEW_YEAR_PROMO_LINKS + PRODUCTS_PAGE_PROMO_LINKS)
def test_guest_can_add_product_to_basket(browser, link):
    """Тест добавления товара в корзину."""
    if link == "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7":
        pytest.xfail("Known_Bag")
    product_page = ProductPage(browser, link)
    product_page.open().add_product_to_basket().solve_quiz_and_get_code()
    product_page.check_product_added_to_basket()


@pytest.mark.negative
def test_guest_cant_see_success_message(browser):
    """Тест отсутствия сообщений при открытии страницы продукта без добавления продукта в корзину"""
    link = PRODUCTS_PAGE_LINK_1
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_alert_success()


@pytest.mark.negative
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    """Негативный Тест сообщения о добавлении продукта в корзину"""
    link = PRODUCTS_PAGE_LINK_1
    product_page = ProductPage(browser, link)
    product_page.open().add_product_to_basket()
    product_page.should_be_alert_disappeared()


@pytest.mark.negative
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """Негативный Тест сообщения о добавлении продукта в корзину"""
    link = PRODUCTS_PAGE_LINK_1
    product_page = ProductPage(browser, link)
    product_page.open().add_product_to_basket()
    product_page.should_not_be_alert_success()
