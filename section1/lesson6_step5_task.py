from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
address = "http://suninjuly.github.io/find_link_text"
text = str(math.ceil(math.pow(math.pi, math.e)*10000))
try:
    browser.get(address)
    link = browser.find_element(By.PARTIAL_LINK_TEXT, text)
    link.click()

    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys('Ivan')

    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys('Ivanov')

    input3 = browser.find_element(By.CLASS_NAME, 'city')
    input3.send_keys('Irkutsk')

    input4 = browser.find_element(By.ID, 'country')
    input4.send_keys('Russia')

    button = browser.find_element(By.CLASS_NAME, 'btn-default')
    time.sleep(1)
    button.click()
finally:
    time.sleep(10)
    browser.quit()
