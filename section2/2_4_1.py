from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time 

try: 
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.set_window_size(1055, 1000)
    browser.get(link)

    # Нажимаем кнопку
    button = browser.find_element(By.ID, "button")
    button.click()



finally:

    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()