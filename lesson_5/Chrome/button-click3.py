from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Клик по кнопке с CSS-классом

driver.maximize_window()

for i in range(3):
    driver.get('http://uitestingplayground.com/classattr')
    driver.find_element(By.CSS_SELECTOR, '.btn-primary.btn-test').click()

    wait = WebDriverWait(driver, timeout=5)
    alert = wait.until(EC.alert_is_present())

    alert.accept()

    sleep(5)
