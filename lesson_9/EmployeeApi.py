import requests
from sqlalchemy import create_engine
from sqlalchemy.sql import text


class EmployeeApi:
    def __init__(self, url) -> None:
        self.url = url
    
    def get_token(self, user='bloom', password='fire-fairy'):
        creds = {
            "username": user,
            "password": password
            } 
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]
    
    def get_company_list(self, params_to_add=None):
        resp = requests.get(self.url + '/company', params=params_to_add)
        return resp.json()
    
    def create_company(self, name, description=""):
        company = {
            "name": name,
            "description": description
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/company',
                             json=company, headers=my_headers)
        return resp.json()

    def get_employee_list(self, params_to_add):

        resp = requests.get(self.url + '/employee', params=params_to_add)
        return resp.json()
    
    def add_new_employee(self, name, last_name, middle_name, companyId, e_email, url, phone, birthdate, isActive):
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
    
    def add_employee_no_token(self, name, last_name, middle_name, companyId, e_email, url, phone, birthdate, isActive):
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

    def get_employee_by_id(self, id):
        resp = requests.get(self.url+ '/employee/'+ str(id))
        return resp.json()      
    
    def edit_employee(self, last_name, email, url, phone, isActive, id):
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