from address import Address
from Mailing import Mailing

to_address = Address(630123, "Novosibirsk", "Lenina", "12", 345)
from_address = Address(177654, "Moscow", "Pushkina", "132б", 15)

to_address.toAddress()
from_address.fromAddress()

Mailing1 = Mailing(to_address, from_address, 500, '098755689455')
Mailing1.whatMailing()

def tracking():
    print("Отправление ", Mailing1.track, "из ", from_address, "в ", to_address, ". Стоимость ", Mailing1.cost, " рублей.")
tracking()
