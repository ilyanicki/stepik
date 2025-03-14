from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/selects1.html"
    browser.get(link)

    number_1 = browser.find_element(By.XPATH, "//span[@id='num1']")
    number_2 = browser.find_element(By.XPATH,"//span[@id='num2']")
    number_3 = int(number_1.text)+int(number_2.text)

    select = Select(browser.find_element(By.XPATH,"//select[@class='custom-select']"))
    select.select_by_visible_text(str(number_3))

    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit_button.click()

    alert_result = browser.switch_to.alert
    print(alert_result.text)

finally:
    browser.quit()

