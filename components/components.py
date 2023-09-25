
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException #исключения прописываем, чтобы можно было вылавливать..
from selenium.webdriver.common.keys import Keys

class WebElement:
    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator

    def click(self):
       self.driver.find_element(By.CSS_SELECTOR, self.locator).click()

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def find_elements(self):
        return self.driver.find_elements(By.CSS_SELECTOR, self.locator)

    def exist(self):
        try:
            self.driver.find_element()
        except NoSuchElementException:
            return False
        return True

    def exist_icon(self):
        try:
            #self.icon.find_element()
            self.driver.find_element()
        except NoSuchElementException:
            return False
        return True

    def visible(self):
        return self.driver.find_element.is_displayed()

    #######################
    def not_visible(self):
        return self.driver.find_element.btn_sidebar_first_checkbox()

    #################
    def check_count_elements(self, count: int) -> bool:
        if len(self.find_element()) == count:
            return True
        return False
    ######################
    def send_keys(self, text: str):
        return self.find_element().send_keys(text)

    def click_force(self):
        self.driver.execute_script("arguments[0].click();", self.find_element())

    def clear(self):
        self.find_element().send_keys(Keys.CONTROL + 'a')
        self.find_element().send_keys(Keys.DELETE)
        self.find_element().send_keys(Keys.ARROW_DOWN)
        self.find_element().send_keys(Keys.ENTER)