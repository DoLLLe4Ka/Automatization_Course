from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, browser):
        self._driver = browser
        self._driver.get('https://www.saucedemo.com/cart.html')
        self._driver.maximize_window()
    
    def fill_form(self, name, last_name, postal_code):
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()
        self._driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(name)
        self._driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(postal_code)
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()

    def check_total_sum(self):
        total = self._driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
        self._driver.quit()
        assert total == 'Total: $58.29'
        print('Total is true')