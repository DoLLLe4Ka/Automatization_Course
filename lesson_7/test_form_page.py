from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from FormPage import FormPage

def test_form_page():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    form_page = FormPage(browser)
    form_page.fill_first_name('Иван')
    form_page.fill_last_name('Петров')
    form_page.fill_address('Ленина, 55-3')
    form_page.fill_email('test@skypro.com')
    form_page.fill_phone('+7985899998787')
    form_page.fill_zip_code('')
    form_page.fill_city('Москва')
    form_page.fill_country('Россия')
    form_page.fill_job('QA')
    form_page.fill_company('SkyPro')
    form_page.submit_button()
    form_page.assert_color()

    browser.quit()