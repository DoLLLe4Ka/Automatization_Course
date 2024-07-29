import allure
from selenium.webdriver.common.by import By
from links import cart_url

class CartPage:
    """
        Этот класс представляет страницу Корзина.
        На этой странице происходит заполнение формы доставки
        и отображение финальной суммы заказа
    """

    def __init__(self, browser):
        """
            Этот метод является конструктором класса.
            Создает аттрибут _driver, который ссылается на объект браузера.
            Принимает на ввод объект browser.
        """ 
        self._driver = browser
        self._driver.get(cart_url)
    
    @allure.step("Заполнение формы доставки")
    def fill_form(self, name: str, last_name: str, postal_code: str)-> None:
        """
            Этот метод заполняет поля формы доставки
            и нажимает на кнопку "Continue"
        """
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()
        self._driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(name)
        self._driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(postal_code)
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()
    
    @allure.step("Проверка итоговой суммы заказа")
    def check_total_sum(self)-> None:
        """
            Этот метод проверяет итоговую сумму на страницу Корзины
            Сравнивает сумму на странице с ожидаемым результатом
        """
        total = self._driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
        self._driver.quit()
        assert total == 'Total: $58.29'
        print('Total is true')