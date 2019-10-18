link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
add_to_basket_button_xpath = '//button[@type="submit" and @class="btn btn-lg btn-primary btn-add-to-basket"]'

def test_add_to_basket_button_exist(browser):
    browser.get(link)
    buttons = browser.find_elements_by_xpath(add_to_basket_button_xpath)
    n_buttons = len(buttons)
    assert n_buttons == 1, "There are {} buttons for adding to basket".format(n_buttons)