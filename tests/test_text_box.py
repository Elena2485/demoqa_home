# a.	перейти на страницу https://demoqa.com/text-box
# b.	записать в поля Full Name, Current Address произвольный текст
# c.	нажать на кнопку submit
# d.	проверить, что снизу появились 2 элемента с нашим текстом
# i.	* сравнение и ввод текста, реализовать через переменную

from pages.text_box import TextBox
from conftest import browser
import time
def test_text_box(browser):
    test_page = TextBox(browser)
    test_page.visit()
    assert not test_page.modal_dialog.exist()
    time.sleep(2)
    test_page.full_name.send_keys('Elena')
    test_page.current_address.send_keys('SPb')
    time.sleep(2)
    test_page.btn_submit.click_force()



