from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    # Метод для получения названия товара
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    # Метод для получения цены товара
    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_success_message(self, expected_name):
        # Проверяем, что название товара в сообщении совпадает с тем, что мы сохранили
        message_text = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME).text
        assert expected_name == message_text, \
            f"Expected product name '{expected_name}', but got '{message_text}'"

    def should_be_basket_total(self, expected_price):
        # Проверяем, что цена в корзине совпадает с ценой товара
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text
        assert expected_price == basket_total, \
            f"Expected basket total '{expected_price}', but got '{basket_total}'"