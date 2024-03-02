"""Модуль содержит тесты ProductPage."""

import pytest
from .pages.product_page import ProductPage
from .pages.pages_links import PRODUCTS_PAGE_LINKS


@pytest.mark.parametrize("link", PRODUCTS_PAGE_LINKS)
def test_guest_can_add_product_to_basket(browser, link):
    """Тест добавления товара в корзину."""
    product_page = ProductPage(browser, link)
    product_page.open().add_product_to_basket().solve_quiz_and_get_code()
    product_page.check_product_added_to_basket()
