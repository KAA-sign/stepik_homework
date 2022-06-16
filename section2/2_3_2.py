from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time 
import math

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.set_window_size(1055, 1000)
    browser.get(link)

    # Нажимаем кнопку
    button = browser.find_element_by_css_selector(".btn")
    button.click()

    # Выбираем вторую вкладку
    new_window = browser.window_handles[1]

    # Переключамся на новую вкладку
    browser.switch_to.window(new_window)

    # Получение значения и расчет
    value = int(browser.find_element_by_id("input_value").text)
    func = math.log(abs(12 * math.sin(value)))

    # Вводим значение в поле
    input = browser.find_element_by_id("answer")
    input.send_keys(str(func))

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # # ждем загрузки страницы
    # time.sleep(5)


finally:

    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()