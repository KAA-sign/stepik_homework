from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class PrductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    PRODUCT_PRISE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#default > div.container-fluid.page > div > ul > li.active")
    CONFIRM_ADD_TO_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    BASKET_PRISE = (By.CSS_SELECTOR, "#content_inner > article > table > tbody > tr:nth-child(3) > td")
    PRODUCT_PRISE_IN_BASKET = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")

