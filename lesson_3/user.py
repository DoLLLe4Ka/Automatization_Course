class User:
    def __init__(self, _first_name, _last_name):
        self.username = _first_name
        self.surname = _last_name
    
    def sayName(self):
        print("Моё имя: ", self.username)
    
    def saySurname(self):
        print("Моя фамилия: ", self.surname)
    
    def sayFullName(self):
        print("Имя и фамилия: ", self.username, self.surname)

user1 = User("Юля", "Петрова")

# user1.sayName()
# user1.saySurname()
# user1.sayFullName()