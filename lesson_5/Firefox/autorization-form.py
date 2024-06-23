# Откройте страницу http://the-internet.herokuapp.com/login.
# В поле username введите значение tomsmith.
# В поле password введите значение SuperSecretPassword!.
# Нажмите кнопку Login.


from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Форма авторизации

driver.get('http://the-internet.herokuapp.com/login')
driver.find_element(By.CSS_SELECTOR, "#username").send_keys("tomsmith")
sleep(1)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("SuperSecretPassword!")
sleep(1)
driver.find_element(By.CSS_SELECTOR, "button").click()

sleep(3)