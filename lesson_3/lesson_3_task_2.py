catalog = []

from smartphone import Smartphone

xiaomi = Smartphone("Xiaomi", "14", "+79999999999")
iPhone = Smartphone("iPhone", "6S", "+79111111111")
samsung = Smartphone("Samsung", "S23", "+79111111112")
pixel = Smartphone("Pixel", "AA", "+79111111113")
honor = Smartphone("Honor", "123", "+79111111114")

catalog.append(xiaomi)
catalog.append(iPhone)
catalog.append(samsung)
catalog.append(pixel)
catalog.append(honor)

for n in catalog:
    print(f'{n.brand} - {n.model}. {n.phoneNumber}')  
       
