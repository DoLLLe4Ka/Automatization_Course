import allure
from Pages.ShopMainPage import MainPage
from Pages.ShopCartPage import CartPage

@allure.title ("Добавление товаров и заполнение формы")
@allure.description(
    """
    "Авторизация, добавление товаров в корзину, 
    заполнение формы доставки и проверка итоговой суммы"
    """)
@allure.feature("Интернет-магазин")
@allure.severity(severity_level='critical')
def test_saucedemo(chrome_browser):
    with allure.step("Открыть главную страницу сайта"):
        main_page = MainPage(chrome_browser)
    with allure.step("Авторизация и добавление в корзину"):
        main_page.authorize('standard_user', 'secret_sauce')
        main_page.add_products()
    with allure.step("Открыть страницу корзины"):
        cart_page = CartPage(chrome_browser)
    with allure.step("Заполнение формы доставки и проверка суммы"):
        cart_page.fill_form('Роберт', 'Халоу', '2837')
        cart_page.check_total_sum()