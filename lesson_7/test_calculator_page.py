from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from CalculatorPage import CalculatorPage

def test_calculator_page():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    calculator_page = CalculatorPage(browser)
    calculator_page.sum('45')
    calculator_page.wait_result('45')
    browser.quit()

