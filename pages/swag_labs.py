from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
class SwagLabs(BasePage):


    def exist_icon(self):
        try:
            self.find_element(locator='div.login_logo')
        except NoSuchElementException:
            return False
        return True

    def click_on_the_icon(self):
        self.find_element(locator='div.login_logo').click()

    def equal_url(self):
        if self.get_url() == 'https://www.saucedemo.com/':
            return True
        return False


