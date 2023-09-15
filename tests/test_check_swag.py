import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome
    yield driver
    driver.quit()

############a.	в файле test_check_swag.py реализуйте следующий тест кейс:
#перейти на страницу https://www.saucedemo.com/
#проверить наличие иконки

from pages.base_page import BasePage
class SwagLabs(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.saucedemo.com/'

 # 6/ перейти на страницу https: // www.saucedemo.com /
 # проверить наличие иконки

    def visit(self):
        return self.driver.get(self.base_url)
        return self.click_on_the_icon(self.base_url)

# 7 в файле test_check_swag.py реализуйте следующий тест кейс:
    # перейти на страницу https://www.saucedemo.com/
    # проверить наличие поля имени
    def find_element(self, locator):
        return self.driver.find_element('div.login_logo', locator)

# 7 / перейти на страницу https://www.saucedemo.com/
# проверить наличие поля пароля

    def get_pass(self):
#return self.driver.get(self.base_url)
        if self.find_element('input#password.input_error.form_input') <> 0
            return True
         return False

