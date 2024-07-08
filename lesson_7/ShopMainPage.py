from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, browser):
        self._driver = browser
        self._driver.get('https://www.saucedemo.com/')
        self._driver.maximize_window()

    def authorize(self, login, password):
        self._driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(login)
        self._driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()
    
    def add_products(self):
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()