"""Модуль содержит PageObject ProductPage"""

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    """Класс PageObject ProductPage"""

    def should_be_btn_add_to_basket(self):
        """Проверка ссылки на кнопку 'Добавить в корзину'."""
        assert self.is_element_present(
            *ProductPageLocators.BTN_ADD_TO_BASKET
        ), "btn_add_to_basket is not presented"

    def should_be_product_name(self):
        """Проверка на наличие текста с именем продукта."""
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "product name is not presented"

    def should_be_product_price(self):
        """Проверка на наличие текста с ценой продукта."""
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "product price is not presented"

    def should_be_alert_success(self):
        """Проверка наличия сообщения с подтверждением добавления продукта в корзину."""
        assert self.is_element_present(*ProductPageLocators.ALERT_SUCCESS), "alert-success is not presented"

    def should_be_alert_info(self):
        """Проверка наличия сообщения с информацией о продукте добавленном в корзину."""
        assert self.is_element_present(*ProductPageLocators.ALERT_INFO), "alert-info is not presented"

    def get_product_name(self):
        """Получение текста с именем продукта."""
        self.should_be_product_name()
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        """Получение текста с ценой продукта."""
        self.should_be_product_price()
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_alert_success_text(self):
        """Получение текста из сообщения с именем продукта добавленного в корзину."""
        self.should_be_alert_success()
        return self.browser.find_element(*ProductPageLocators.ALERT_SUCCESS_TXT).text

    def get_alert_info_text(self):
        """Получение текста из сообщения с ценой продукта добавленного в корзину."""
        self.should_be_alert_info()
        return self.browser.find_element(*ProductPageLocators.ALERT_INFO_TXT).text

    def add_product_to_basket(self):
        """Нажатие кнопки 'добавить в корзину'."""
        self.should_be_btn_add_to_basket()
        self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET).click()
        return self

    def check_product_name_added_to_basket(self):
        """Проверка равенства имени продукта и текста с именем продукта добавленного в корзину."""
        product_name = self.get_product_name()
        alert_success_text = self.get_alert_success_text()
        assert (
            product_name == alert_success_text
        ), f"product name = {product_name} is not equal in alert_success_text = {alert_success_text}"

    def check_product_price_added_to_basket(self):
        """Проверка равенства цены продукта и текста с ценой продукта добавленного в корзину."""
        product_price = self.get_product_price()
        alert_info_text = self.get_alert_info_text()
        assert (
            product_price == alert_info_text
        ), f"product price = {product_price}  is not equal in alert_info_text = {alert_info_text}"

    def check_product_added_to_basket(self):
        """Проверка равенства продукта и текста сообщения о продукте добавленном в корзину."""
        self.check_product_name_added_to_basket()
        self.check_product_price_added_to_basket()
