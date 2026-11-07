from selenium.webdriver.common.by import By


def test_product_has_add_to_basket_button(browser):
    browser.get("https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    buttons = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert len(buttons) == 1, "Expected one add to basket button"
