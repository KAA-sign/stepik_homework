import pytest
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators

import time


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])

# @pytest.mark.xfail(reason="incorrect parameter promo")
# def test_guest_can_add_product_to_basket(browser, link):
#     page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#     page.open()                      # открываем страницу
#     page.add_to_basket()
#     # time.sleep(60)
#     page.solve_quiz_and_get_code()
#     page.check_price_and_nane_product_in_basket()
    

# @pytest.mark.xfail()
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    # page.solve_quiz_and_get_code()
    # time.sleep(60)
    page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)
    

# @pytest.mark.xfail()
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    # page.solve_quiz_and_get_code()
    page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

# @pytest.mark.xfail()
def test_message_disappeared_after_adding_product_to_basket(browser, link):  
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)

