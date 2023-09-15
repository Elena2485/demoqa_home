import pytest
from selenium import webdriver

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


    def visit(self):
        return self.driver.get(self.base_url)
    click_on_the_icon()

    def find_element(self, locator):
        time.sleep(3)  # задержка на 3 секунды
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def get_url(self):
        return self.driver.current_url
