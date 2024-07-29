from sqlalchemy import create_engine
from sqlalchemy.sql import text
import allure


class EmployeeTable:
    """
        Этот класс представляет таблицу Employees
        в базе данных. 
    """
    __scripts = {
        "select": text("select * from employee where \"company_id\" = :company_id"),
        "delete company by id": text("delete from company where id =:id_to_delete_1"),
        "delete employee by id": text("delete from employee where id =:id_to_delete_2"),
        "insert new company": text("insert into company(name) values (:new_name)"),
        "insert new employee": text("insert into employee(is_active, first_name, last_name, middle_name, phone, email, birthdate, avatar_url, company_id) values (:is_active, :first_name, :last_name, :middle_name, :phone, :email, :birthdate, :avatar_url, :company_id)"),
        "get max company id": text("select MAX(id) from company where deleted_at is null"),
        "select by id": text("select * from employee where id =:select_id and deleted_at is null")
    }


    def __init__(self, connection_string):
        """
            Этот метод принимает аргумент connection_string
            и создает движок для подключения к базе
        """
        self.__db = create_engine(connection_string).connect()

    @allure.step("БД. Получение списка сотрудников")
    def get_employees(self, company_id):
        """
            Этот метод принимает id компании
            и выдает список сотрудников
        """
        return self.__db.execute(self.__scripts["select"], {"company_id" : company_id}).fetchall()

    @allure.step("БД. Добавление компании")
    def add_company(self, name):
        """
            Этот метод принимает название компании,
            создает компанию и возвращает её id
        """
        self.__db.execute(self.__scripts["insert new company"], {"new_name" : name})
        self.__db.commit()
        return self.__db.scalar(self.__scripts["get max company id"])
    
    @allure.step("БД. Получение информации о сотруднике")
    def get_employee_by_id(self, id):
        """
            Этот метод возвращает информацию
            о сотруднике по id
        """
        self.__db.execute(self.__scripts["select by id"], {"select_id" : id})
    
    @allure.step("БД. Добавление сотрудника")
    def add_employee(self, employee):
        """
            Этот метод принимает на ввод словарь с информацией
            о сотруднике и создает нового сотрудника
        """
        self.__db.execute(
            self.__scripts["insert new employee"],
            {
                "is_active": employee["is_active"],
                "first_name": employee["first_name"],
                "last_name": employee["last_name"],
                "middle_name": employee["middle_name"],
                "phone": employee["phone"],
                "email": employee["email"],
                "birthdate": employee["birthdate"],
                "avatar_url": employee["avatar_url"],
                "company_id": employee["company_id"]
            }
        )
        self.__db.commit()
    

    @allure.step("БД. Удаление компании")
    def delete(self, id):
        """
            Этот метод принимает id компании и удаляет компанию
        """        
        self.__db.execute(self.__scripts["delete company by id"], {"id_to_delete_1": id})
    

    @allure.step("БД. Удаление сотрудника")
    def delete_employee(self, id):
        """
            Этот метод принимает id сотрудника и удаляет сотрудника
        """  
        self.__db.execute(self.__scripts["delete employee by id"], {"id_to_delete_2": id})