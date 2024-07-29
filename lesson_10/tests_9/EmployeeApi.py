import allure
import requests
from links import url

class EmployeeApi:
    """
        Этот класс представляет сущность 
        для работы с сотрудниками.
    """
    def __init__(self, url=url) -> None:
        """
            Это метод инициализации.
            Принимает url.
        """
        self.url = url
    

    @allure.step("api. Получение токена авторизации")
    def get_token(self, user='bloom', password='fire-fairy')-> str:
        """
            Этот метод принимает логин и пароль
            и возвращает токен авторизации
        """
        creds = {
            "username": user,
            "password": password
            } 
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]
    

    @allure.step("api. Получение списка компаний")
    def get_company_list(self, params_to_add=None) -> list:
        """
            Этот метод принимает params_to_add
            и возвращает список компаний
        """
        resp = requests.get(self.url + '/company', params=params_to_add)
        return resp.json()
    

    @allure.step("api. Создание новой компании")
    def create_company(self, name: str, description="")-> dict:
        """
            Этот метод принимает имя и описание 
            и создает новую компанию.
        """
        company = {
            "name": name,
            "description": description
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/company',
                             json=company, headers=my_headers)
        return resp.json()
    

    @allure.step("api. Получение списка сотрудников")
    def get_employee_list(self, params_to_add: int):
        """
            Этот метод принимает params_to_add (id компанию) 
            и возвращает список сотрудников.
        """
        resp = requests.get(self.url + '/employee', params=params_to_add)
        return resp.json()
    

    @allure.step("api. Добавление нового сотрудника")
    def add_new_employee(
        self, name: str, last_name: str, middle_name: str, companyId: int, e_email: str, url: str, phone: str, birthdate: str, isActive: bool
        )-> dict:
        """
            Этот метод создает нового сотрудника.
            
        """
        employee = {
            "firstName": name,
            "lastName": last_name,
            "middleName": middle_name,
            "companyId": companyId,
            "email": e_email,
            "url": url,
            "phone": phone,
            "birthdate": birthdate,
            "isActive": isActive
        }

        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/employee',
                             json=employee, headers=my_headers)
        return resp.json()
    

    @allure.step("api. Добавление сотрудника без токена")
    def add_employee_no_token(self, name, last_name, middle_name, companyId, e_email, url, phone, birthdate, isActive):
        """
            Этот метод отправляет словарь с данными нового сотрудника
            без токена авторизации.
            Для тестирования попытки неавторизованного доступа. 
        """
        employee = {
        "firstName": name,
        "lastName": last_name,
        "middleName": middle_name,
        "companyId": companyId,
        "email": e_email,
        "url": url,
        "phone": phone,
        "birthdate": birthdate,
        "isActive": isActive
        }

        resp = requests.post(self.url + '/employee', json=employee)
        return resp.json()
    

    @allure.step("api. Получение сотрудника по id")
    def get_employee_by_id(self, id: int):
        """
            Этот метод принимает id сотрудника
            и возвращает словарь с данными сотрудника.
        """

        resp = requests.get(self.url+ '/employee/'+ str(id))
        return resp.json()      
    

    @allure.step("api. Редактирование данных сотрудника")
    def edit_employee(self, last_name: str, email: str, url: str, phone: str, isActive: bool, id: int)-> dict:
        """
            Этот метод принимает на вход данные сотрудника
            и редактирует информацию о нем. 
            Необходимо передать id для редактирования.
        """
        employee = {
            "lastName": last_name,
            "email": email,
            "url": url,
            "phone": phone,
            "isActive": isActive
        }

        my_headers = {}
        my_headers["x-client-token"] = self.get_token()

        resp = requests.patch(self.url + '/employee/'+ str(id),
                             json=employee, headers=my_headers)
        return resp.json()