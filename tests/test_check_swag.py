
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

############a.	в файле test_check_swag.py реализуйте следующий тест кейс:
#перейти на страницу https://www.saucedemo.com/
#проверить наличие иконки

from pages.base_page import BasePage
class SwagLabs(BasePage):

    # 6/ перейти на страницу https: // www.saucedemo.com /
    # проверить наличие иконки
    def exist_icon(browser):
        browser.get('https://www.saucedemo.com/')
        swag_labs_page = SwagLabs(browser)
        swag_labs_page.visit()
        swag_labs_page.click_on_the_icon()
        assert swag_labs_page.exist_icon()


# 7 в файле test_check_swag.py реализуйте следующий тест кейс:
    # перейти на страницу https://www.saucedemo.com/
    # проверить наличие поля имени
    def check_name(browser):
        browser.get('https://www.saucedemo.com/')
        swag_labs_page = SwagLabs(browser)
        swag_labs_page.visit()

        try:
            swag_labs_page.find_element(By.CSS_SELECTOR, '#user-name')
        except NoSuchElementException:
            assert False
        assert True

# 7 / перейти на страницу https://www.saucedemo.com/
# проверить наличие поля пароля

    def check_field_pass(browser):
        browser.get('https://www.saucedemo.com/')
        swag_labs_page = SwagLabs(browser)
        swag_labs_page.visit()

        try:
            swag_labs_page.find_element(By.CSS_SELECTOR, '#password')
        except NoSuchElementException:
            assert False
        assert True

