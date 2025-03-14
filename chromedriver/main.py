from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
import os
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button_trollface = browser.find_element(By.CSS_SELECTOR, ".trollface")
    button_trollface.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    number = browser.find_element(By.CSS_SELECTOR,"#input_value")

    input_number = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_number.send_keys(calc(number.text))

    button_submit = browser.find_element(By.CSS_SELECTOR,".btn")
    button_submit.click()

    alert_result = browser.switch_to.alert
    print(alert_result.text)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()