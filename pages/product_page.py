from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):

    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()

    def check_price_and_nane_product_in_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRISE).text
        add_to_basket_answer = self.browser.find_element(*ProductPageLocators.CONFIRM_ADD_TO_BASKET).text
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRISE_IN_BASKET).text
        assert product_name == add_to_basket_answer, "Product not in basket"
        assert product_price in product_price_in_basket, "Product price and basket price are not equal"
        

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.find_element(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
    

    


 