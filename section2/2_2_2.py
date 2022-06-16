from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.set_window_size(1055, 1000)
    browser.get(link)


    # Получение значения и расчет
    value = int(browser.find_element_by_id("input_value").text)
    func = math.log(abs(12 * math.sin(value)))

    # Прокручиваем страницу
    browser.execute_script("window.scrollBy(0, 200);")

    # Вводим значение в поле
    input = browser.find_element_by_id("answer")
    input.send_keys(str(func))

    # Нажимаем checkbox
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    # Нажимаем radiobutton
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(5)


finally:

    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


