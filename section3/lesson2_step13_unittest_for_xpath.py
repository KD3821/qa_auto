import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestCorrect(unittest.TestCase):
    def test_string(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)
            input1 = browser.find_element(By.XPATH, '//div[@class="first_block"]/div[contains(@class,"first_class")]/input')
            input1.send_keys('Denis')
            input2 = browser.find_element(By.XPATH,
                                          '//div[@class="first_block"]/div[contains(@class, "second_class")]/input')
            input2.send_keys('Denisov')
            input3 = browser.find_element(By.XPATH,
                                          '//div[@class="first_block"]/div[contains(@class, "third_class")]/input')
            input3.send_keys('mail@mail.com')
            time.sleep(3)
            button = browser.find_element(By.XPATH, '//button[contains(@class, "btn")]')
            button.click()
            time.sleep(3)
            reply = browser.find_element(By.TAG_NAME, 'h1')
            welcome = reply.text
            self.assertEqual(welcome, "Congratulations! You have successfully registered!", "reg not success")
        finally:
            browser.quit()

    def test_string2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)
            input1 = browser.find_element(By.XPATH, '//div[@class="first_block"]/div[contains(@class,"first_class")]/input')
            input1.send_keys('Denis')
            input2 = browser.find_element(By.XPATH,
                                          '//div[@class="first_block"]/div[contains(@class, "second_class")]/input')
            input2.send_keys('Denisov')
            input3 = browser.find_element(By.XPATH,
                                          '//div[@class="first_block"]/div[contains(@class, "third_class")]/input')
            input3.send_keys('mail@mail.com')
            time.sleep(3)
            button = browser.find_element(By.XPATH, '//button[contains(@class, "btn")]')
            button.click()
            time.sleep(3)
            reply = browser.find_element(By.TAG_NAME, 'h1')
            welcome = reply.text
            self.assertEqual(welcome, "Congratulations! You have successfully registered!", "reg2 not success")
        finally:
            browser.quit()


if __name__ == "__main__":
    unittest.main()
