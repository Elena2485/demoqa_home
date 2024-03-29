

from pages.base_page import BasePage
from components.components import WebElement

class ModalDialog(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.elements = WebElement(driver, '#header-text')
        self.current_address = WebElement(driver, '#currentAddress')
        self.btn_submit = WebElement(driver, '#body > div.fade.modal.show > div')