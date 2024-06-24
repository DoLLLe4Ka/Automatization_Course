import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_calculator(driver):
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
    driver.find_element(By.CSS_SELECTOR, "#delay").clear()
    driver.find_element(By.CSS_SELECTOR, "#delay").send_keys('45')
    driver.find_element(By.XPATH, '//span[contains(text(), "7")]').click()
    driver.find_element(By.XPATH, '//span[contains(text(), "+")]').click()
    driver.find_element(By.XPATH, '//span[contains(text(), "8")]').click()
    driver.find_element(By.XPATH, '//span[contains(text(), "=")]').click()

    waiter = WebDriverWait(driver, 45, 0.1)
    # Код не отрабатывает со значением 45 секунд, отрабатывает со значением 45.1
    result = waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.screen'), '15')
    )
    assert result == True
    print("Assertion passed, result is 15.")


