from selenium.webdriver.common.by import By
class FormPage:
    def __init__(self, browser):
        self._driver = (browser)
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
        self._driver.maximize_window()
    
    def fill_first_name(self, text):
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="first-name"]').send_keys(text)
    def fill_last_name(self, text):
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="last-name"]').send_keys(text)
    def fill_address(self, text):
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="address"]').send_keys(text)
    def fill_email(self, text):
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="e-mail"]').send_keys(text)
    def fill_phone(self, text):
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="phone"]').send_keys(text)
    def fill_zip_code(self, text):
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="zip-code"]').send_keys(text)
    def fill_city(self, text):
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="city"]').send_keys(text)
    def fill_country(self, text):
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="country"]').send_keys(text)
    def fill_job(self, text):
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="job-position"]').send_keys(text)
    def fill_company(self, text):
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="company"]').send_keys(text)
    def submit_button(self):
        self._driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-outline-primary.mt-3').click()

    def assert_color(self):
        red_color = self._driver.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property('background-color')
        assert red_color == 'rgba(248, 215, 218, 1)'
        
        green_color = self._driver.find_element(By.CSS_SELECTOR, '#first-name').value_of_css_property('background-color')
        assert green_color == 'rgba(209, 231, 221, 1)'

        green_color = self._driver.find_element(By.CSS_SELECTOR, '#last-name').value_of_css_property('background-color')
        assert green_color == 'rgba(209, 231, 221, 1)'

        green_color = self._driver.find_element(By.CSS_SELECTOR, '#address').value_of_css_property('background-color')
        assert green_color == 'rgba(209, 231, 221, 1)'

        green_color = self._driver.find_element(By.CSS_SELECTOR, '#e-mail').value_of_css_property('background-color')
        assert green_color == 'rgba(209, 231, 221, 1)'

        green_color = self._driver.find_element(By.CSS_SELECTOR, '#phone').value_of_css_property('background-color')
        assert green_color == 'rgba(209, 231, 221, 1)'

        green_color = self._driver.find_element(By.CSS_SELECTOR, '#city').value_of_css_property('background-color')
        assert green_color == 'rgba(209, 231, 221, 1)'

        green_color = self._driver.find_element(By.CSS_SELECTOR, '#country').value_of_css_property('background-color')
        assert green_color == 'rgba(209, 231, 221, 1)'

        green_color = self._driver.find_element(By.CSS_SELECTOR, '#job-position').value_of_css_property('background-color')
        assert green_color == 'rgba(209, 231, 221, 1)'

        green_color = self._driver.find_element(By.CSS_SELECTOR, '#company').value_of_css_property('background-color')
        assert green_color == 'rgba(209, 231, 221, 1)'
    
    
