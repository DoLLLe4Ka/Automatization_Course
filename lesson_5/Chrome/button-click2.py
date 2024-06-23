from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Клик по кнопке без ID
driver.maximize_window()
for x in range(3):
    driver.get('http://uitestingplayground.com/dynamicid')
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()
    sleep(5)