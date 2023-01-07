from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.XPATH, '//input[@name="firstname"]')
    input2 = browser.find_element(By.XPATH, '//input[@name="lastname"]')
    input3 = browser.find_element(By.XPATH, '//input[@name="email"]')
    input1.send_keys('Ivan')
    input2.send_keys('Ivanov')
    input3.send_keys('mail@mail.com')
    file_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(file_dir, 'test.txt')
    file_upload = browser.find_element(By.ID, 'file')
    file_upload.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    time.sleep(2)
    button.click()
    time.sleep(5)
finally:
    browser.quit()
