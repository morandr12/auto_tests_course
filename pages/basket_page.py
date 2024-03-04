"""Модуль содержит PageObject BasketPage"""

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket_message(self):
        """Проверка присутствия сообщения о пустой корзине."""
        assert self.is_element_present(
            *BasketPageLocators.EMPTY_BASKET_MESSAGE
        ), "Empty_basket_message is not presented"
        return self

    def should_not_be_basket_formset(self):
        """Проверка отсутствия формы с товарами."""
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_FORMSET
        ), "Basket_formset is presented"
        return self
