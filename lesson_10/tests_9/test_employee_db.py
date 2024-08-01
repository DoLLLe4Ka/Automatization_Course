import pytest
import allure
from EmployeeApi import EmployeeApi
from EmployeeDatabase import EmployeeTable

api = EmployeeApi("https://x-clients-be.onrender.com")
db = EmployeeTable("postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")


@allure.title ("Получение списка сотрудников")
@allure.description("Получение и сравнение списка сотрудников через api и из базы")
@allure.feature("Получение списка")
@allure.severity(severity_level='critical')
def test_get_employee_list():
    with allure.step("Получение списка компаний"):
        company_list = api.get_company_list()
        with allure.step("Получение id последней компании"):
            company_id = company_list[-1]["id"]
            params_to_add = {
                'company': company_id
            }
        api_list = api.get_employee_list(params_to_add)
        db_result = db.get_employees(company_id)
    with allure.step("Сравнение списков api и базы данных"):
        assert len(api_list) == len(db_result)


@allure.title ("Получение списка сотрудников без id компании")
@allure.description("Получение списка сотрудников без указания id компании")
@allure.feature("Получение списка")
@allure.severity(severity_level='major')
def test_get_employee_list_without_company_id():
    with allure.step("Передача пустых параметров"):
        params_to_add = None
    with allure.step("Получение списка сотрудников"):    
        employees = api.get_employee_list(params_to_add)
    with allure.step("Проверка сообщения об ошибке"): 
        assert employees['message'] == "Internal server error"


@allure.title ("Получение списка сотрудников с неверным id")
@allure.description("Получение списка сотрудников с указанием неверного id компании")
@allure.feature("Получение списка")
@allure.severity(severity_level='major')
def test_get_employee_list_with_wrong_company_id():
    with allure.step("Создание параметров"): 
        params_to_add = {
            'company': 8989898
        }
    with allure.step("Получение списка сотрудников"): 
        full_list = api.get_employee_list(params_to_add)
    with allure.step("Проверка, что число сотрудников =0"): 
        assert len(full_list) == 0


@allure.title ("Добавление нового сотрудника")
@allure.description("Добавление нового сотрудника в существущую компанию")
@allure.feature("Добавление сотрудника")
@allure.severity(severity_level='critical')
def test_add_new_employee():
    with allure.step("Получение id компании"):
        company_list = api.get_company_list()
        company_id = company_list[0]["id"]
        params_to_add = {
            'company': company_id
        }
    with allure.step("Вычисление длины списка сотрудников"):
        list_before = api.get_employee_list(params_to_add)
        len_before = len(list_before)
    
    with allure.step("Создание сотрудника"):
        with allure.step("Заполнение данных сотрудника"):
            name = "Peter"
            last_name = "Pen"
            middle_name = "John"
            companyId = int(company_id)
            e_email = "test37@mail.ru"
            url = "https://123.com"
            phone = "89998887766"
            birthdate = "2024-12-08"
            isActive = True
        with allure.step("Добавление сотрудника"):
            new_employee = api.add_new_employee(name, last_name, middle_name, companyId,
                                        e_email, url, phone, birthdate, isActive)
            with allure.step("Получение id нового сотрудника"):
                new_id = new_employee["id"]
    with allure.step("Вычисление длины списка сотрудников"):
        final_list = api.get_employee_list(params_to_add)
        len_after = len(final_list)

    with allure.step("Выполнение проверок"):
            with allure.step("Проверить, что список сотрудников увеличился на 1"):
                assert len_after - len_before == 1
            with allure.step("Проверить, что последний id в списке равен id нового сотрудника"):
                assert final_list[-1]["id"] == new_id

    with allure.step("Удаление созданного сотрудника"):
        db.delete_employee(new_id)


@allure.title ("Добавление нового сотрудника в новую компанию")
@allure.description("Создание новой компании и добавление в неё нового сотрудника")
@allure.feature("Добавление сотрудника")
@allure.severity(severity_level='critical')
def test_add_new_employee_to_new_company():
    with allure.step("Создание компании"):
        name = 'NBA'
        company_id = db.add_company(name)
        with allure.step("Вычисление id новой компании"):
            params_to_add = {
                'company': company_id
            }
    with allure.step("Создание сотрудника"):
        with allure.step("Записать данные сотрудника"):
            employee = {
                "first_name": "Peter",
                "last_name": "Pen",
                "middle_name": "John",
                "company_id": company_id,
                "email": "test@gmail.com",
                "avatar_url": "https://123.com",
                "phone": "1234567899",
                "birthdate": "2024-12-08",
                "is_active": True
            }
        
        db.add_employee(employee)
        with allure.step("Получение списка сотрудников"):
            api_list = api.get_employee_list(params_to_add)
            db_list = db.get_employees(company_id)
            with allure.step("Вычисление id нового сотрудника"):
                new_id = db_list[0][0]
    with allure.step("Проведение проверок"):
        with allure.step("Проведение проверок"):
            with allure.step(
                "Проверить, что список сотрудников, полученнный из базы данных=1"
                ):
                assert len(db_list) == 1
            with allure.step(
                "Проверить, что список сотрудников, полученнный с помощью api=1"
                ):
                assert len(api_list) == 1
            with allure.step(
                "Проверить, что id сотрудника из списка совпадает с id нового сотрудника"
                ):
                assert api_list[0]["id"] == new_id
    with allure.step("Удаление тестовых сущностей"):
        db.delete_employee(new_id)
        db.delete(company_id)


@allure.title ("Добавление сотрудника без id компании")
@allure.description(
    "Отправка запроса на добавление сотрудника без id компании, проверка ошибки"
    )
@allure.feature("Добавление сотрудника")
@allure.severity(severity_level='critical')
def test_add_new_employee_without_company_id():
    with allure.step("Создание сотрудника"):
        with allure.step("Запись данных сотрудника"):
            name = "Peter"
            last_name = "Pen"
            middle_name = "John"
            companyId = None
            email = "dollle4ka@mail.ru"
            url = "https://123.com"
            phone = "1234567899"
            birthdate = "2024-12-08"
            isActive = True
        new_employee = api.add_new_employee(name, last_name, middle_name, 
                                        companyId, email, url, phone, 
                                        birthdate, isActive)
    with allure.step("Проверка сообщения об ошибке"):
        assert new_employee['message'] == 'Internal server error'


@allure.title ("Добавление сотрудника без токена")
@allure.description(
    "Добавление нового сотрудника без токена авторизации"
    )
@allure.feature("Добавление сотрудника")
@allure.severity(severity_level='critical')
def test_add_employee_no_token():
    with allure.step("Создание компании и получение id"):
        company_name = "ABC"
        result = api.create_company(company_name)
        company_id = result["id"]
    with allure.step("Создание сотрудника"):
        with allure.step("Запись данных сотрудника"):
            name = "Pitty"
            last_name = "Pen"
            middle_name = "John"
            companyId = int(company_id)
            email = "test@gmail.com"
            url = "https://123.com"
            phone = "89998887766"
            birthdate = "2024-12-08"
            isActive = True

        new_employee = api.add_employee_no_token(name, last_name, middle_name, 
                                            companyId, email, url, phone,
                                            birthdate, isActive)
    with allure.step("Проверить статус ошибки"):
        assert new_employee["statusCode"] == 401


@pytest.mark.xfail(reason='''ФР: Не сохраняется email при создании сотрудника,
ошибка Assertion Error, ОР: При создании сотрудника сохраняется введенный email,
assertion проходит успешно''')
@allure.title ("Получение информации о сотруднике")
@allure.description(
    "Получение информации о сотруднике по id"
    )
@allure.feature("Получение сотрудника")
@allure.severity(severity_level='critical')
def test_get_employee_by_id():
    with allure.step("Создание компании"):
        name = 'NBA'
        company_id = db.add_company(name)

    with allure.step("Создание сотрудника"):
        with allure.step("Запись данных сотрудника"):
            employee = {
                "first_name": "Peter",
                "last_name": "Pen",
                "middle_name": "John", 
                "company_id": company_id,
                "email": "test@gmail.com",
                "avatar_url": "https://123.com",
                "phone": "89998887766",
                "birthdate": "2024-12-08",
                "is_active": True
            }
        with allure.step("Добавление сотрудника"):
            db.add_employee(employee)
            db_list = db.get_employees(company_id)
            new_id = db_list[0][0]

    with allure.step("Получение сотрудника по id"):
        body = api.get_employee_by_id(new_id)
    with allure.step("Проверка данных сотрудника"):
            with allure.step("Проверка значения first_name"):
                assert body["firstName"] == employee["first_name"]
            with allure.step("Проверка значения last_name"):
                assert body["lastName"] == employee["last_name"]
            with allure.step("Проверка значения middle_name"):
                assert body["middleName"] == employee["middle_name"]
            with allure.step("Проверка значения company_id"):
                assert body["companyId"] == employee["company_id"]
            with allure.step("Проверка значения avatar_url"):
                assert body["avatar_url"] == employee["avatar_url"]
            with allure.step("Проверка значения phone"):
                assert body["phone"] == employee["phone"]
            with allure.step("Проверка значения birthdate"):
                assert body["birthdate"] == employee["birthdate"]
            with allure.step("Проверка значения is_active"):
                assert body["isActive"] == employee["is_active"]
            with allure.step("Проверка значения id"):
                assert body["id"] == new_id
            with allure.step("Проверка значения email"):
                assert body["email"] == employee["email"]
    with allure.step("Удаление сотрудника и компании"):
        db.delete_employee(new_id)
        db.delete(company_id)

@allure.title ("Получение сотрудника без id")
@allure.description(
    "Получение информации о сотруднике без передачи id"
    )
@allure.feature("Получение сотрудника")
@allure.severity(severity_level='critical')
def test_get_employee_without_id():
    with allure.step("Проверка сообщения об ошибке"):
        try:
            api.get_employee_by_id()
        except TypeError as e:
            assert str(e) == "EmployeeApi.get_employee_by_id() missing 1 required positional argument: 'id'"


@pytest.mark.xfail(reason="ФР: Не редактируется номер телефона, ОР: Редактируется номер телефона")
@allure.title ("Редактирование данных сотрудника")
@allure.description(
    "Редактирование информации о сотруднике"
    )
@allure.feature("Редактирование сотрудника")
@allure.severity(severity_level='critical')
def test_edit_employee():
    with allure.step("Создание компании"):
        name = 'NBA'
        company_id = db.add_company(name)
    
    with allure.step("Создание сотрудника"):
        with allure.step("Запись данных сотрудника"):
            employee = {
                "first_name": "Peter",
                "last_name": "Pen",
                "middle_name": "John", 
                "company_id": company_id,
                "email": "test@gmail.com",
                "avatar_url": "https://123.com",
                "phone": "89998887766",
                "birthdate": "2024-12-08",
                "is_active": True
            }
    with allure.step("Добавление сотрудника"):
        db.add_employee(employee)
        db_list = db.get_employees(company_id)
        new_id = db_list[0][0]

    with allure.step("Редактирование данных сотрудника"):
        with allure.step("Запись новых данных"):
            last_name = "Kitty"
            email = "test123@gmail.com"
            url = "https://567.com"
            phone = "89112223344"
            isActive = False

        api.edit_employee(last_name, email, url, phone, isActive, new_id)

    body = api.get_employee_by_id(new_id)
    with allure.step("Проверка измененных данных"):
            with allure.step("Проверка last_name"):          
                assert body["lastName"] == last_name
            with allure.step("Проверка email"): 
                assert body["email"] == email
            with allure.step("Проверка phone"): 
                assert body["phone"] == phone
            with allure.step("Проверка avatar_url"): 
                assert body["avatar_url"] == url
            with allure.step("Проверка is_active"): 
                assert body["isActive"] == False
    with allure.step("Удаление сотрудника и компании"):
        db.delete_employee(new_id)
        db.delete(company_id)


@pytest.mark.xfail(reason="ФР: Не редактируется номер телефона, ОР: Редактируется номер телефона")
@allure.title ("Редактирование данных сотрудника с пустым запросом")
@allure.description(
    "Редактирование информации о сотруднике путем отправки запроса без тела запроса"
    )
@allure.feature("Редактирование сотрудника")
@allure.severity(severity_level='major')
def test_edit_employee_without_body_request():
    with allure.step("Проверка сообщения об ошибке"):
        try:
            api.add_new_employee()
        except TypeError as e:
            assert str(e) == (
                "EmployeeApi.add_new_employee() missing 9 required positional arguments: 'name', 'last_name', 'middle_name', 'companyId', 'e_email', 'url', 'phone', 'birthdate', and 'isActive'"
                )

