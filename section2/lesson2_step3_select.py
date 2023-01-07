from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = 'http://suninjuly.github.io/selects1.html'
# link = 'http://suninjuly.github.io/selects2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = int(browser.find_element(By.ID, 'num1').text)
    num2 = int(browser.find_element(By.ID, 'num2').text)
    my_sum = str(num1 + num2)
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(my_sum)
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn' )
    button.click()
    time.sleep(5)
finally:
    browser.quit()
