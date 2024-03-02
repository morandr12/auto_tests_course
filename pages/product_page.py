from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_btn_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), "btn_add_to_basket is not presented"

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "product name is not presented"

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "product price is not presented"

    def should_be_alert_success(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_SUCCESS), "alert-success is not presented"

    def should_be_alert_info(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_INFO), "alert-info is not presented"

    def get_product_name(self):
        self.should_be_product_name()
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        self.should_be_product_price()
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_alert_success_text(self):
        self.should_be_alert_success()
        return self.browser.find_element(*ProductPageLocators.ALERT_SUCCESS_TXT).text

    def get_alert_info_text(self):
        self.should_be_alert_info()
        return self.browser.find_element(*ProductPageLocators.ALERT_INFO_TXT).text

    def add_product_to_basket(self):
        self.should_be_btn_add_to_basket()
        self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET).click()
        return self

    def check_product_name_added_to_basket(self):
        product_name = self.get_product_name()
        alert_success_text = self.get_alert_success_text()
        assert product_name in alert_success_text, "product name not found in alert_success"

    def check_product_price_added_to_basket(self):
        product_price = self.get_product_price()
        alert_info_text = self.get_alert_info_text()
        assert product_price == alert_info_text, "product price is not equal in alert_success"

    def check_product_added_to_basket(self):
        self.check_product_name_added_to_basket()
        self.check_product_price_added_to_basket()
