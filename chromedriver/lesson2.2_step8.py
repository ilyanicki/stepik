from selenium import webdriver
from selenium.webdriver.common.by import By



try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    file_path = "/home/ilya/PycharmProjects/test/chromedriver/file.txt"
    first_name = browser.find_element(By.CSS_SELECTOR, "input.form-control:nth-child(2)")
    first_name.send_keys("ILYA")
    last_name = browser.find_element(By.CSS_SELECTOR, "input.form-control:nth-child(4)")
    last_name.send_keys("NICK")
    email = browser.find_element(By.CSS_SELECTOR, "input.form-control:nth-child(6)")
    email.send_keys("ILYA@mail.ru")

    input_file = browser.find_element(By.CSS_SELECTOR, "#file")
    input_file.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

    alert = browser.switch_to.alert
    print(alert.text)
finally:
    browser.quit()