from selenium import webdriver
from selenium.webdriver.common.by import By
import time



browser = webdriver.Chrome()
browser.get("https://www.degreesymbol.net/")
time.sleep(3)
# link = browser.find_element(By.LINK_TEXT, "Degree Symbol in Math")
link = browser.find_element(By.PARTIAL_LINK_TEXT, "Math")
link.click()
time.sleep(3)
browser.quit()