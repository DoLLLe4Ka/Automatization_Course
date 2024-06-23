from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

# Клик по кнопке

driver.maximize_window()
driver.get('http://the-internet.herokuapp.com/add_remove_elements/')

for x in range(1, 6):
    driver.find_element(By.CSS_SELECTOR, '[onclick="addElement()"]').click()

buttons = driver.find_elements(By.CSS_SELECTOR, '[onclick="deleteElement()"]')
print(len(buttons))

sleep(3)

# Закрытие браузера

driver.quit()

    