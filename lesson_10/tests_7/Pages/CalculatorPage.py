import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from typing import Union
from links import calculator_url

class CalculatorPage:
    """
        Этот класс представляет страницу Калькулятор.
        При помощи калькулятора можно вводить числа 
        и осуществлять с ними арифметические операции
    """
    def __init__(self, browser):
        """
            Этот метод является конструктором класса.
            Создает аттрибут _driver, который ссылается на объект браузера.
            Принимает на ввод объект browser.
            Открывает указанный URL.
        """
        self._driver = browser
        self._driver.get(calculator_url)
    
    def sum(self, txt: Union[int, float])-> Union[int, float]:
        """
            Этот метод запускает ожидание,
            принимает на ввод количество секунд ожидания, 
            вводит числа и вычисляет их сумму
        """
        with allure.step("Ввод времени ожидания"):
            self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
            self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(txt)
        with allure.step("Ввод чисел для вычисления"):
            self._driver.find_element(By.XPATH, '//span[contains(text(), "7")]').click()
            self._driver.find_element(By.XPATH, '//span[contains(text(), "+")]').click()
            self._driver.find_element(By.XPATH, '//span[contains(text(), "8")]').click()
            self._driver.find_element(By.XPATH, '//span[contains(text(), "=")]').click()
    
    @allure.step("Сравнение вычисленной суммы с ожидаемым результатом")
    def wait_result (self, txt: int)-> None:
        """
            Этот метод запускает ожидание пока не исчезнет спиннер,
            после этого сравнивает вычисленную сумму с ожидаемым результатом
        """
        with allure.step("Ожидание, пока спиннер не станет невидимым"):
            locator = (By.CSS_SELECTOR, '#spinner')
            waiter = WebDriverWait(self._driver, txt, 0.1)
            waiter.until(
            EC.invisibility_of_element_located(locator)
            )
        with allure.step("Проверка результата"):
            result = self._driver.find_element(By.CSS_SELECTOR, 'div.screen').text
            assert int(result) == 15
            print("Assertion passed, result is 15.")