from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")

    number = browser.find_element(By.CSS_SELECTOR,"#input_value")

    input_x = browser.find_element(By.XPATH, "//input[@id='answer']")
    input_x.send_keys(str(calc(int(number.text))))

    checkbox = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
    checkbox.click()

    radio_button_robots = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
    radio_button_robots.click()

    button_submit = browser.find_element(By.XPATH, "//button[@type='submit']")
    button_submit.click()

    alert_result = browser.switch_to.alert
    print(alert_result.text)

finally:
    time.sleep(1)
    browser.quit()