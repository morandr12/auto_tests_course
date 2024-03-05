import time
from .pages.product_page import ProductPage
from .pages.pages_links import PRODUCTS_PAGE_LINK_1
from .pages.locators import ProductPageLocators


def test_items(browser):
    """Тест наличия на странице товара кнопки добавления в корзину."""
    link = PRODUCTS_PAGE_LINK_1
    product_page = ProductPage(browser, link)
    product_page.open()
    time.sleep(30)
    assert product_page.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET)
