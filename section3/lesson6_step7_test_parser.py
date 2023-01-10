from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

'''
pytest -s -v lesson6_step7_test_parser.py (exit with error: _pytest.config.UsageError: --browser_name should be chrome or firefox)
pytest -s -v --browser_name=chrome lesson6_step7_test_parser.py
pytest -s -v --browser_name=firefox lesson6_step7_test_parser.py
'''