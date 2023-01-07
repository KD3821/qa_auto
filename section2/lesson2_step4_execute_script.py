from selenium import webdriver
import time


try:
    browser = webdriver.Chrome()
    time.sleep(3)
    browser.execute_script("document.title='Script going down';alert('Robots at work!');")
    time.sleep(3)
finally:
    browser.quit()
