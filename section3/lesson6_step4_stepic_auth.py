from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://stepik.org/lesson/236895/step/1"

def test_login_stepic(browser):
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
