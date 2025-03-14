from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/find_xpath_form"

    browser.get(link)

    first_name_input = browser.find_element(By.XPATH, "//input[@name='first_name']")
    first_name_input.send_keys("ilya")

    last_name_input = browser.find_element(By.XPATH, "//input[@name='last_name']")
    last_name_input.send_keys("nick")

    city_input = browser.find_element(By.XPATH, "//input[@class='form-control city']")
    city_input.send_keys("ulsk")

    country_input = browser.find_element(By.XPATH, "//input[@id='country']")
    country_input.send_keys("russia")

    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    alert = browser.switch_to.alert
    print(alert.text)
finally:
    time.sleep(2)
    browser.quit()