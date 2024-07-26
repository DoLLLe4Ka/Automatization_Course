from sqlalchemy import create_engine
from sqlalchemy.sql import text


class EmployeeTable:
    __scripts = {
        "select": text("select * from employee where \"company_id\" = :company_id"),
        "delete company by id": text("delete from company where id =:id_to_delete"),
        "delete employee by id": text("delete from employee where id =:id_to_delete"),
        "insert new company": text("insert into company(name) values (:new_name)"),
        "insert new employee": text("insert into employee(is_active, first_name, last_name, middle_name, phone, email, birthdate, avatar_url, company_id) values (:is_active, :first_name, :last_name, :middle_name, :phone, :email, :birthdate, :avatar_url, :company_id)"),
        "get max id": text("select MAX(id) from employee where\"company_id\" = :company_id"),
        "get max company id": text("select MAX(id) from company where deleted_at is null"),
        "select by id": text("select * from employee where id =:select_id and deleted_at is null")
    }


    def __init__(self, connection_string):
        self.__db = create_engine(connection_string).connect()
    
    def get_employees(self, company_id):
        return self.__db.execute(self.__scripts["select"], {"company_id" : company_id}).fetchall()
    
    def add_company(self, name):
        self.__db.execute(self.__scripts["insert new company"], {"new_name" : name})
        self.__db.commit()
        return self.__db.scalar(self.__scripts["get max company id"])
    
    def get_employee_by_id(self, id):
        self.__db.execute(self.__scripts["select by id"], {"select_id" : id})

    def add_employee(self, employee):
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

    def get_max_id(self, company_id):
        self.__db.execute(self.__scripts["get max id"], {"company_id" : company_id}).fetchall()[0][0]
    
    def get_max_company_id(self):
        return self.__db.execute(self.__scripts["get max id"]).fetchall()[0][0]
    
    def delete(self, id):
        self.__db.execute(self.__scripts["delete by id"], {"id_to_delete": id})
    
    def delete_employee(self, id):
        self.__db.execute(self.__scripts["delete by id"], {"id_to_delete": id})