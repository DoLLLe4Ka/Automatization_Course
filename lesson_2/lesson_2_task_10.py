def bank():
    i = 0.1
    x = int(input("Введите сумму вклада: "))
    y = int(input("Введите срок вклада: "))
    sum = x*(1+i)**y
    print(round(sum, 2))
bank()