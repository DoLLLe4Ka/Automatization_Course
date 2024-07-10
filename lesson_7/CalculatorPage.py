from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class CalculatorPage:
    def __init__(self, browser):
        self._driver = browser
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        self._driver.maximize_window()
    
    def sum(self, txt):
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(txt)
        self._driver.find_element(By.XPATH, '//span[contains(text(), "7")]').click()
        self._driver.find_element(By.XPATH, '//span[contains(text(), "+")]').click()
        self._driver.find_element(By.XPATH, '//span[contains(text(), "8")]').click()
        self._driver.find_element(By.XPATH, '//span[contains(text(), "=")]').click()

    def wait_result (self, txt):
        locator = (By.CSS_SELECTOR, '#spinner')
        waiter = WebDriverWait(self._driver, txt, 0.1)
        # Код не отрабатывает со значением 45 секунд, отрабатывает со значением 45.1
        waiter.until(
        EC.invisibility_of_element_located(locator)
        )
        result = self._driver.find_element(By.CSS_SELECTOR, 'div.screen').text
        assert int(result) == 15
        print("Assertion passed, result is 15.")