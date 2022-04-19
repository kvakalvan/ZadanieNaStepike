import time



def test_add_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    b = browser.find_element_by_class_name('btn-add-to-basket').text
    time.sleep(5)
    assert b is not None, "Кнопка не найдена"
