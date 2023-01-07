from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    time.sleep(1)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    time.sleep(1)
    button.click()
finally:
    browser.quit()

'''
Другие возможные параметры метода можно посмотреть 
здесь: https://developer.mozilla.org/ru/docs/Web/API/Element/scrollIntoView
// пример скрипта на javascript
button = document.getElementsByTagName("button")[0];
button.scrollIntoView(true);
'''