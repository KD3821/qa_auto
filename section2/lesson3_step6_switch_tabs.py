from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, 'button.trollface')
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    val = browser.find_element(By.CSS_SELECTOR, 'span#input_value')
    y = calc(int(val.text))
    my_input = browser.find_element(By.CSS_SELECTOR, 'input#answer')
    my_input.send_keys(y)
    button2 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button2.click()
    time.sleep(3)
finally:
    browser.quit()