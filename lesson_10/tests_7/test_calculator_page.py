import pytest
import allure
from Pages.CalculatorPage import CalculatorPage

@allure.title ("Вычисление суммы")
@allure.description("Ввод данных и вывод результата вычисления")
@allure.feature("Калькулятор")
@allure.severity(severity_level='blocker')
@pytest.mark.xfail(result="Код не отрабатывает со значением 45 секунд, отрабатывает со значением 45.1")
def test_calculator_page(chrome_browser):
    with allure.step("Открыть калькулятор"):
        calculator_page = CalculatorPage(chrome_browser)
    with allure.step("Ввести значения и вычислить сумму"):
        calculator_page.sum('45')
    with allure.step("Сравнить фактический результат с ожидаемым и закрыть браузер"):
        calculator_page.wait_result('45')
