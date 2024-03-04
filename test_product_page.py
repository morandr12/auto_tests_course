"""Модуль содержит тесты ProductPage."""

import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.locators import ProductPageLocators
from .pages.pages_links import PRODUCTS_PAGE_LINKS, PRODUCTS_PAGE_PROMO_LINK


@pytest.mark.parametrize("link", PRODUCTS_PAGE_LINKS)
def test_guest_can_add_product_to_basket(browser, link):
    """Тест добавления товара в корзину."""
    if link == PRODUCTS_PAGE_PROMO_LINK + "7":
        pytest.xfail("Bag")
    product_page = ProductPage(browser, link)
    product_page.open().add_product_to_basket().solve_quiz_and_get_code()
    product_page.check_product_added_to_basket()


@pytest.mark.parametrize("link", PRODUCTS_PAGE_LINKS)
def test_guest_should_see_login_link_on_product_page(browser, link):
    """Тест наличия ссылки на LoginPage"""
    product_page = ProductPage(browser, link)
    product_page.open().should_be_login_link()


@pytest.mark.parametrize("link", PRODUCTS_PAGE_LINKS)
def test_guest_can_go_to_login_page_from_product_page(browser, link):
    """Тест перехода на страницу логина."""
    product_page = ProductPage(browser, link)
    product_page.open().go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.parametrize("link", PRODUCTS_PAGE_LINKS)
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):
    """Тест перехода на страницу пустой корзины."""
    product_page = ProductPage(browser, link)
    product_page.open().go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_basket_formset().should_be_empty_basket_message()


@pytest.mark.negative
@pytest.mark.skip
@pytest.mark.parametrize("link", PRODUCTS_PAGE_LINKS)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    """Негативный Тест сообщения о добавлении продукта в корзину"""
    product_page = ProductPage(browser, link)
    product_page.open().add_product_to_basket()
    assert product_page.is_not_element_present(
        *ProductPageLocators.ALERT_SUCCESS
    ), "alert-success is presented"


@pytest.mark.negative
@pytest.mark.parametrize("link", PRODUCTS_PAGE_LINKS)
def test_guest_cant_see_success_message(browser, link):
    """Тест отсутствия сообщений при открытии страницы продукта без добавления продукта в корзину"""
    product_page = ProductPage(browser, link)
    product_page.open()
    assert product_page.is_not_element_present(
        *ProductPageLocators.ALERT_SUCCESS
    ), "alert-success is presented"


@pytest.mark.negative
@pytest.mark.skip
@pytest.mark.parametrize("link", PRODUCTS_PAGE_LINKS)
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    """Негативный Тест сообщения о добавлении продукта в корзину"""
    product_page = ProductPage(browser, link)
    product_page.open().add_product_to_basket()
    assert product_page.is_disappeared(*ProductPageLocators.ALERT_SUCCESS), "alert-success is presented"
