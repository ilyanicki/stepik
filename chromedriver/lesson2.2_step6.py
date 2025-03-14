

from selenium import webdriver
from selenium.webdriver.common.by import By
import math




def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, "#input_value")

    x_value = x.text

    input_x = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_x.send_keys(calc(x_value))

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    radio_button = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio_button.click()

    button.click()

    alert_result = browser.switch_to.alert
    print(alert_result.text)
finally:
    browser.quit()
