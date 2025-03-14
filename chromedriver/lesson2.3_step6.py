from selenium import webdriver
from selenium.webdriver.common.by import By
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    button_1 = browser.find_element(By.CSS_SELECTOR, ".trollface")
    button_1.click()

    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element(By.CSS_SELECTOR,"#input_value")

    input_x = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_x.send_keys(calc(x.text))

    button_2 = browser.find_element(By.CSS_SELECTOR, ".btn")
    button_2.click()

    alert = browser.switch_to.alert
    print(alert.text)

finally:
    browser.quit()