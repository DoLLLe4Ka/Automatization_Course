import allure
from selenium.webdriver.common.by import By
from links import form_url

class FormPage:
    """
        Этот класс представляет страницу Веб-форма
        с различными полями для заполнения
    """
    def __init__(self, browser):
        """
            Этот метод является конструктором класса.
            Создает аттрибут _driver, который ссылается на объект браузера.
            Принимает на ввод объект browser.
            Открывает указанный URL
        """
        self._driver = (browser)
        self._driver.get(form_url)

    @allure.step("Заполнение поля First name")
    def fill_first_name(self, text: str)-> None:
        """
            Этот метод вводит данные в поле "First name"
        """
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="first-name"]').send_keys(text)

    @allure.step("Заполнение поля Last name")
    def fill_last_name(self, text:str)-> None:
        """
            Этот метод вводит данные в поле "Last name".
        """
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="last-name"]').send_keys(text)
    
    @allure.step("Заполнение поля Address")
    def fill_address(self, text: str)-> None:
        """
            Этот метод вводит данные в поле "Address".
        """
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="address"]').send_keys(text)

    @allure.step("Заполнение поля e-mail")
    def fill_email(self, text: str)-> None:
        """
            Этот метод вводит данные в поле "e-mail".
        """        
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="e-mail"]').send_keys(text)

    @allure.step("Заполнение поля phone")
    def fill_phone(self, text: str)-> None:
        """
            Этот метод вводит данные в поле "phone".
        """  
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="phone"]').send_keys(text)

    @allure.step("Заполнение поля zip-code")
    def fill_zip_code(self, text: str)-> None:
        """
            Этот метод вводит данные в поле "zip-code".
        """  
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="zip-code"]').send_keys(text)

    @allure.step("Заполнение поля City")
    def fill_city(self, text: str)-> None:
        """
            Этот метод вводит данные в поле "City".
        """  
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="city"]').send_keys(text)

    @allure.step("Заполнение поля Country")
    def fill_country(self, text: str)-> None:
        """
            Этот метод вводит данные в поле "Country".
        """  
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="country"]').send_keys(text)

    @allure.step("Заполнение поля Job-position")
    def fill_job(self, text: str)-> None:
        """
            Этот метод вводит данные в поле "Job-position".
        """  
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="job-position"]').send_keys(text)

    @allure.step("Заполнение поля Company")
    def fill_company(self, text: str)-> None:
        """
            Этот метод вводит данные в поле "Company".
        """  
        self._driver.find_element(By.CSS_SELECTOR, '.form-control[name="company"]').send_keys(text)

    @allure.step("Нажатие на кнопку Submit")
    def submit_button(self)-> None:
        """
            Этот метод нажимает на кнопку "Submit".
        """          
        self._driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-outline-primary.mt-3').click()

    @allure.step("Проверка цвета полей")
    def assert_color(self)-> None:
        """
            Этот метод проверяет, что поля подсвечиваются соответствующими цветами.
            Заполненные валидными данными поля должно подсвечиваться зеленым,
            незаполненное поле должно подсвечиваться красным. 
        """  
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
    
    
