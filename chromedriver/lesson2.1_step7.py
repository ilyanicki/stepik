import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math




def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    treasure = browser.find_element(By.XPATH, "//img[@id='treasure']")

    input_x = browser.find_element(By.XPATH, "//input[@id='answer']")
    input_x.send_keys(calc(treasure.get_attribute("valuex")))

    checkbox = browser.find_element(By.XPATH,"//input[@id='robotCheckbox']")
    checkbox.click()

    radiobutton = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
    radiobutton.click()

    button_submit = browser.find_element(By.CSS_SELECTOR, ".btn")
    button_submit.click()

    alert_result = browser.switch_to.alert
    print(alert_result.text)
finally:
    time.sleep(10)
    browser.quit()