from .base_page import BasePage
from .locators import PrductPageLocators
import time


class ProductPage(BasePage):

    def add_to_basket(self):
        basket_button = self.browser.find_element(*PrductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()

    def check_price_and_nane_product_in_basket(self):
        # time.sleep(60)
        product_name = self.browser.find_element(*PrductPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*PrductPageLocators.PRODUCT_PRISE).text
        add_to_basket_answer = self.browser.find_element(*PrductPageLocators.CONFIRM_ADD_TO_BASKET).text
        product_price_in_basket = self.browser.find_element(*PrductPageLocators.PRODUCT_PRISE_IN_BASKET).text
        assert product_name in add_to_basket_answer, "Product not in basket"
        assert product_price in product_price_in_basket, "Product price and basket price are not equal"

    

    


 