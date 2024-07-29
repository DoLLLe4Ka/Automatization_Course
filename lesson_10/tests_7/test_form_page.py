import allure
from Pages.FormPage import FormPage

@allure.title ("Заполнение и отправка веб-формы")
@allure.description("Заполнение полей формы, проверка фона полей после заполнения")
@allure.feature("Веб-форма")
@allure.severity(severity_level='critical')
def test_form_page(chrome_browser):
    with allure.step("Открытие браузера"):
        form_page = FormPage(chrome_browser)
    with allure.step("Заполнение формы и проверка цвета полей"):
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
