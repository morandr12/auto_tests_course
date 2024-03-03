"""Модуль содержит тесты ProductPage."""

import pytest
from .pages.product_page import ProductPage
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


@pytest.mark.negative
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
    """Негативный Тест открытия страницы продукта без добавления продукта в корзину"""
    product_page = ProductPage(browser, link)
    product_page.open()
    assert product_page.is_not_element_present(
        *ProductPageLocators.ALERT_SUCCESS
    ), "alert-success is presented"


@pytest.mark.negative
@pytest.mark.parametrize("link", PRODUCTS_PAGE_LINKS)
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    """Негативный Тест сообщения о добавлении продукта в корзину"""
    product_page = ProductPage(browser, link)
    product_page.open().add_product_to_basket()
    assert product_page.is_disappeared(
        *ProductPageLocators.ALERT_SUCCESS
    ), "alert-success is presented"
