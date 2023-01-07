from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button = browser.find_element(By.CSS_SELECTOR, 'button#book')
    button.click()

    val = browser.find_element(By.CSS_SELECTOR, 'span#input_value')
    x = calc(int(val.text))
    my_input = browser.find_element(By.ID, 'answer')
    my_input.send_keys(x)
    bttn = browser.find_element(By.CSS_SELECTOR, 'button#solve')
    bttn.click()
    time.sleep(3)
finally:
    browser.quit()
