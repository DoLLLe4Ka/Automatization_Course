from address import Address
from mailing import Mailing

to_address = Address("155810", "Кинешма", "ул. им. Урицкого", "4", "99")
from_address = Address("115554", "Москва", "ул. 8 Марта", "48", "54")

mailing = Mailing(to_address, from_address, 100, "1234567890")

print(f'Отправление {mailing.track} из {from_address.index}, {from_address.city}, {from_address.street}, {from_address.house} - {from_address.flat} в\
 {to_address.index}, {to_address.city}, {to_address.street}, {to_address.house} - {to_address.flat}. Стоимость {mailing.cost} рублей.')
