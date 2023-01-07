from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(3)
    x_label = browser.find_element(By.ID, 'input_value')
    x = x_label.text
    y = calc(x)
    input = browser.find_element(By.CSS_SELECTOR, '#answer')
    input.send_keys(y)
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    radio = browser.find_element(By.CSS_SELECTOR, 'input#robotsRule')
    radio.click()
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    time.sleep(3)
    button.click()
    time.sleep(5)
finally:
    browser.quit()
