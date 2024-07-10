from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from ShopMainPage import MainPage
from ShopCartPage import CartPage

def test_saucedemo():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    main_page = MainPage(browser)
    main_page.authorize('standard_user', 'secret_sauce')
    main_page.add_products()
    cart_page = CartPage(browser)
    cart_page.fill_form('Роберт', 'Халоу', '2837')
    cart_page.check_total_sum()
    browser.quit()