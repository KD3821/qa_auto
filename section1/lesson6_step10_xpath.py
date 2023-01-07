from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"  # test should pass
    # link = "http://suninjuly.github.io/registration2.html"  # test should fail

    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.XPATH, '//div[@class="first_block"]/div[contains(@class,"first_class")]/input')
    input1.send_keys('Denis')
    input2 = browser.find_element(By.XPATH, '//div[@class="first_block"]/div[contains(@class, "second_class")]/input')
    input2.send_keys('Denisov')
    input3 = browser.find_element(By.XPATH, '//div[@class="first_block"]/div[contains(@class, "third_class")]/input')
    input3.send_keys('mail@mail.com')
    time.sleep(3)
    button = browser.find_element(By.XPATH, '//button[contains(@class, "btn")]')
    button.click()
    time.sleep(3)
    string1 = "Congratulations! You have successfully registered!"
    reply = browser.find_element(By.TAG_NAME, 'h1')
    welcome = reply.text
    assert string1 == welcome
    time.sleep(2)
finally:
    browser.quit()
