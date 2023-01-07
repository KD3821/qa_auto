from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, 'input')
    a = 1
    for i in elements:
        i.send_keys('Yo'+ str(a))
        a += 1

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-default')
    button.click()
finally:
    time.sleep(10)
    browser.quit()
