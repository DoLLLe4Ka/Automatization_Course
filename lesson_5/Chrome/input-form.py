from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Поле ввода

driver.get('http://the-internet.herokuapp.com/inputs')
driver.find_element(By.CSS_SELECTOR, "input").send_keys("1000")

sleep(3)

driver.find_element(By.CSS_SELECTOR, "input").clear()

sleep(3)

driver.find_element(By.CSS_SELECTOR, "input").send_keys("999")

sleep(3)