from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    element = browser.find_element(By.ID, 'treasure')
    x = element.get_attribute('valuex')
    val = calc(x)
    input = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    input.send_keys(val)
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    radio = browser.find_element(By.CSS_SELECTOR, 'input#robotsRule')
    radio.click()
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
    time.sleep(5)
finally:
    browser.quit()
