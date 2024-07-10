import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_form_filling(driver):
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    driver.find_element(By.CSS_SELECTOR, '.form-control[name="first-name"]').send_keys('Иван')
    driver.find_element(By.CSS_SELECTOR, '.form-control[name="last-name"]').send_keys('Петров')
    driver.find_element(By.CSS_SELECTOR, '.form-control[name="address"]').send_keys('Ленина, 55-3')
    driver.find_element(By.CSS_SELECTOR, '.form-control[name="e-mail"]').send_keys('test@skypro.com')
    driver.find_element(By.CSS_SELECTOR, '.form-control[name="phone"]').send_keys('+7985899998787')
    driver.find_element(By.CSS_SELECTOR, '.form-control[name="zip-code"]').send_keys('')
    driver.find_element(By.CSS_SELECTOR, '.form-control[name="city"]').send_keys('Москва')
    driver.find_element(By.CSS_SELECTOR, '.form-control[name="country"]').send_keys('Россия')
    driver.find_element(By.CSS_SELECTOR, '.form-control[name="job-position"]').send_keys('QA')
    driver.find_element(By.CSS_SELECTOR, '.form-control[name="company"]').send_keys('SkyPro')

    driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-outline-primary.mt-3').click()

    red_color = driver.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property('background-color')
    print(red_color)
    assert red_color == 'rgba(248, 215, 218, 1)'
    print("Assertion passed, background color is red.")

    green_color = driver.find_element(By.CSS_SELECTOR, '#first-name').value_of_css_property('background-color')
    print(green_color)
    assert green_color == 'rgba(209, 231, 221, 1)'
    print("Assertion passed, background color is green.")

    green_color = driver.find_element(By.CSS_SELECTOR, '#last-name').value_of_css_property('background-color')
    assert green_color == 'rgba(209, 231, 221, 1)'
    print("Assertion passed, background color is green.")

    green_color = driver.find_element(By.CSS_SELECTOR, '#address').value_of_css_property('background-color')
    assert green_color == 'rgba(209, 231, 221, 1)'
    print("Assertion passed, background color is green.")

    green_color = driver.find_element(By.CSS_SELECTOR, '#e-mail').value_of_css_property('background-color')
    assert green_color == 'rgba(209, 231, 221, 1)'
    print("Assertion passed, background color is green.")

    green_color = driver.find_element(By.CSS_SELECTOR, '#phone').value_of_css_property('background-color')
    assert green_color == 'rgba(209, 231, 221, 1)'
    print("Assertion passed, background color is green.")

    green_color = driver.find_element(By.CSS_SELECTOR, '#city').value_of_css_property('background-color')
    assert green_color == 'rgba(209, 231, 221, 1)'
    print("Assertion passed, background color is green.")

    green_color = driver.find_element(By.CSS_SELECTOR, '#country').value_of_css_property('background-color')
    assert green_color == 'rgba(209, 231, 221, 1)'
    print("Assertion passed, background color is green.")

    green_color = driver.find_element(By.CSS_SELECTOR, '#job-position').value_of_css_property('background-color')
    assert green_color == 'rgba(209, 231, 221, 1)'
    print("Assertion passed, background color is green.")

    green_color = driver.find_element(By.CSS_SELECTOR, '#company').value_of_css_property('background-color')
    assert green_color == 'rgba(209, 231, 221, 1)'
    print("Assertion passed, background color is green.")
