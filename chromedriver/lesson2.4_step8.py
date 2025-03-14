from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
    button = browser.find_element(By.CSS_SELECTOR, "#book")
    button.click()

    x = browser.find_element(By.CSS_SELECTOR, "#input_value")
    input_x = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_x.send_keys(calc(x.text))

    submit_button = browser.find_element(By.CSS_SELECTOR, "#solve")
    submit_button.click()

    alert = browser.switch_to.alert
    print(alert.text)
finally:
    browser.quit()