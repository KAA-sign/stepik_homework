import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
time.sleep(30)


def test_guest_should_see_add_to_basket_batton(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_elements_by_css_selector("button.btn-add-to-basket"), "Кнопкпка добавления в корзину осутствует" 