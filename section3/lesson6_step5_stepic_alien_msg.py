import pytest
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

links_lst = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]


@pytest.mark.parametrize('link', links_lst)
def test_login_stepic(browser, link):
    browser.get(link)
    login_bttn = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a#ember33')))
    login_bttn.click()
    sign_in_bttn = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.sign-form__btn')))
    username = 'mymail@mail.com'
    passw = 'NotMyPassword'
    input1 = browser.find_element(By.CSS_SELECTOR, 'input#id_login_email')
    input2 = browser.find_element(By.CSS_SELECTOR, 'input#id_login_password')
    input1.send_keys(username)
    input2.send_keys(passw)
    sign_in_bttn.click()
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'img.navbar__profile-img')))
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea')))
    try:
        browser.find_element(By.CSS_SELECTOR, 'div.attempt__score-info')
        again_bttn = browser.find_element(By.CSS_SELECTOR, 'button.again-btn')
        again_bttn.click()
    except NoSuchElementException:
        pass
    input3 = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'textarea')))
    answer = math.log(int(time.time()))
    input3.send_keys(answer)
    send_bttn = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.submit-submission')))
    send_bttn.click()
    feedback = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'p.smart-hints__hint')))
    fb_text = feedback.text
    assert fb_text == "Correct!", f"Ответ не подходит :( - {fb_text}"

