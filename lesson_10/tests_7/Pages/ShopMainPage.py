import allure
from selenium.webdriver.common.by import By
from links import main_url

class MainPage:
    """
        Этот класс представляет главную страницу сайта.
        На этой странице происходит авторизация
        и добавление продуктов в корзину
    """
    def __init__(self, browser):
        """
            Этот метод является конструктором класса.
            Создает аттрибут _driver, который ссылается на объект браузера.
            Принимает на ввод объект browser, открывает указанный url.
        """    
        self._driver = browser
        self._driver.get(main_url)
    
    @allure.step("Прохождение авторизации")
    def authorize(self, login: str, password: str)-> None:
        """
            Этот метод отвечает за авторизацию.
            Вводит логин и пароль, нажимает на кнопку Login. 
        """
        self._driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(login)
        self._driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()
    
    @allure.step("Добавление товаров в корзину")
    def add_products(self) ->None:
        """
            Этот метод добавляет товары в корзину
            нажатием на кнопку Add to cart. 
        """
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()