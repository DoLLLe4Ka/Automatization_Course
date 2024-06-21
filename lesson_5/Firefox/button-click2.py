from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Клик по кнопке без ID
driver.maximize_window()
for x in range(3):
    driver.get('http://uitestingplayground.com/dynamicid')
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
    sleep(5)

# Закрытие браузера

driver.quit()