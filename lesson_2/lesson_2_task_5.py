def month_to_season():
        n = int(input("Введите номер месяца: "))
        if (n == 12) or (n <= 2):
             print("Зима")
        elif (n >=3) and (n < 6):
            print("Весна")
        elif (n >= 6) and (n < 9):
            print("Лето")
        elif (n >= 9) and (n < 12):
            print("Осень")
month_to_season()

