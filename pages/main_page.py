"""Модуль содержит PageObject MainPage"""
from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    """Класс PageObject MainPage"""
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
