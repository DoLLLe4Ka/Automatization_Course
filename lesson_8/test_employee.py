import requests
import pytest
from EmployeeApi import EmployeeApi

api = EmployeeApi("https://x-clients-be.onrender.com")

def test_get_employee_list():

    company_list = api.get_company_list()
    company_id = company_list[0]["id"]
    params_to_add = {
        'company' : company_id
    }
    full_list = api.get_employee_list(params_to_add)
    assert len(full_list) > 0

def test_get_employee_list_without_company_id():
    params_to_add = None
    employees = api.get_employee_list(params_to_add)
    assert employees['message'] == "Internal server error"

def test_get_employee_list_with_wrong_company_id():
    params_to_add = {
        'company' : 8989898
    }
    full_list = api.get_employee_list(params_to_add)
    assert len(full_list) == 0

def test_add_new_employee():
    company_list = api.get_company_list()
    company_id = company_list[0]["id"]
    params_to_add = {
        'company' : company_id
    }
    list_before = api.get_employee_list(params_to_add)
    len_before = len(list_before)
    
    name = "Peter"
    last_name = "Pen"
    middle_name = "John" 
    companyId = int(company_id)
    e_email = "dollle4ka@mail.ru"
    url = "https://123.com"
    phone = "1234567899"
    birthdate = "2024-12-08"
    isActive = True

    new_employee = api.add_new_employee(name, last_name, middle_name, companyId, e_email, url, phone, birthdate, isActive)
    new_id = new_employee["id"]

    final_list = api.get_employee_list(params_to_add)
    len_after = len(final_list)
    assert len_after - len_before == 1
    assert final_list[-1]["id"] == new_id

def test_add_new_employee_without_company_id():  
    name = "Peter"
    last_name = "Pen"
    middle_name = "John"
    companyId = None
    e_email = "dollle4ka@mail.ru"
    url = "https://123.com"
    phone = "1234567899"
    birthdate = "2024-12-08"
    isActive = True  

    new_employee = api.add_new_employee(name, last_name, middle_name, companyId, e_email, url, phone, birthdate, isActive)
    assert new_employee['message'] == 'Internal server error'

def test_add_new_employee_to_new_company():
    company_name = "NBA"
    result = api.create_company(company_name)
    company_id = result["id"]

    params_to_add = {
        'company' : company_id
    }
    
    name = "Peter"
    last_name = "Pen"
    middle_name = "John" 
    companyId = int(company_id)
    e_email = "test@gmail.com"
    url = "https://123.com"
    phone = "1234567899"
    birthdate = "2024-12-08"
    isActive = True

    new_employee = api.add_new_employee(name, last_name, middle_name, companyId, e_email, url, phone, birthdate, isActive)
    new_id = new_employee["id"]

    final_list = api.get_employee_list(params_to_add)
    assert final_list[-1]["id"] == new_id

def test_add_employee_no_token():
    company_name = "ABC"
    result = api.create_company(company_name)
    company_id = result["id"]
    
    name = "Pitty"
    last_name = "Pen"
    middle_name = "John"
    companyId = int(company_id)
    e_email = "test@gmail.com"
    url = "https://123.com"
    phone = "89998887766"
    birthdate = "2024-12-08"
    isActive = True

    new_employee = api.add_employee_no_token(name, last_name, middle_name, companyId, e_email, url, phone, birthdate, isActive)
    assert new_employee["statusCode"] == 401

@pytest.mark.xfail(reason="ФР: Не сохраняется email при создании сотрудника, ошибка Assertion Error, ОР: При создании сотрудника сохраняется введенный email, assertion проходит успешно")
def test_get_employee_by_id():
    #Cоздаем компанию
    company_name = "For id"
    result = api.create_company(company_name)
    company_id = result["id"]

    #Создаем сотрудника
    name = "Peter"
    last_name = "Pen"
    middle_name = "John" 
    companyId = int(company_id)
    e_email = 'dollle4ka@mail.ru'
    url = "https://123.com"
    phone = "89165555555"
    birthdate = "2024-12-08"
    isActive = True

    new_employee = api.add_new_employee(name, last_name, middle_name, companyId, e_email, url, phone, birthdate, isActive)
    new_id = new_employee["id"]

    # Получаем сотрудника по id
    body = api.get_employee_by_id(new_id)

    assert body["firstName"] == name
    assert body["lastName"] == last_name
    assert body["middleName"] == middle_name
    assert body["companyId"] == companyId
    assert body["avatar_url"] == url
    assert body["phone"] == phone
    assert body["birthdate"] == birthdate
    assert body["isActive"] == True
    assert body["id"] == new_id
    assert body["email"] == e_email

def test_get_employee_without_id():
    try:
        api.get_employee_by_id()
    except TypeError as e:
        assert str(e) == "EmployeeApi.get_employee_by_id() missing 1 required positional argument: 'id'"

@pytest.mark.xfail(reason="ФР: Не редактируется номер телефона, ОР: Редактируется номер телефона")
def test_edit_employee():
    #Cоздаем компанию
    company_name = "For editing"
    result = api.create_company(company_name)
    company_id = result["id"]

    #Создаем сотрудника
    name = "Peter"
    last_name = "Pen"
    middle_name = "John" 
    companyId = int(company_id)
    e_email = 'dollle4ka@mail.ru'
    url = "https://123.com"
    phone = "89165555555"
    birthdate = "2024-12-08"
    isActive = True

    new_employee = api.add_new_employee(name, last_name, middle_name, companyId, e_email, url, phone, birthdate, isActive)
    id = new_employee["id"]
    # Редактируем данные сотрудника
    last_name = "Kitty"
    email = "test123@gmail.com"
    url = "https://567.com"
    phone = "89112223344"
    isActive = False

    edited_emp = api.edit_employee(last_name, email, url, phone, isActive, id)

    body = api.get_employee_by_id(id)

    assert body["lastName"] == last_name
    assert body["email"] == email
    assert body["phone"] == phone
    assert body["avatar_url"] == url
    assert body["isActive"] == False

def test_edit_employee_without_body_request():
    try:
        new_employee = api.add_new_employee()
    except TypeError as e:
        assert str(e) == "EmployeeApi.add_new_employee() missing 9 required positional arguments: 'name', 'last_name', 'middle_name', 'companyId', 'e_email', 'url', 'phone', 'birthdate', and 'isActive'"