from NovaPoshta.ApiModels.Counterparty import Counterparty
from NovaPoshta.MethodParameters.Counterparty_cloneLoyaltyCounterpartySender import \
    Counterparty_cloneLoyaltyCounterpartySender
from NovaPoshta.MethodParameters.Counterparty_getCounterparties import Counterparty_getCounterparties
from NovaPoshta.MethodParameters.Counterparty_getCounterpartyAddresses import Counterparty_getCounterpartyAddresses
from NovaPoshta.MethodParameters.Counterparty_getCounterpartyByEDRPOU import Counterparty_getCounterpartyByEDRPOU
from NovaPoshta.MethodParameters.Counterparty_getCounterpartyContactPersons import \
    Counterparty_getCounterpartyContactPersons
from NovaPoshta.MethodParameters.Counterparty_getCounterpartyOptions import Counterparty_getCounterpartyOptions
from NovaPoshta.MethodParameters.MethodParameters import MethodParameters

__author__ = 'chen'

def save():
    counterparty = Counterparty()
    counterparty.setCounterpartyProperty('Recipient')\
        .setCityRef('db5c88d0-391c-11dd-90d9-001a92567626')\
        .setCounterpartyType('PrivatePerson')\
        .setFirstName('Пилипко')\
        .setLastName('Вася')\
        .setMiddleName('Сергеевич')\
        .setPhone('+380661122333')\
        .setEmail('test@i.ua')

    return counterparty.save()

def save2():
    counterparty = Counterparty()
    counterparty.setCityRef('8d5a980d-391c-11dd-90d9-001a92567626')\
        .setCounterpartyType('Organization')\
        .setEDRPOU('00000000')

    return counterparty.saveThirdPerson()

def update():
    counterparty = Counterparty()
    counterparty.setRef('eb863d12-ac7d-11e4-a77a-005056887b8d')\
        .setCounterpartyProperty('Recipient')\
        .setCityRef('db5c88d0-391c-11dd-90d9-001a92567626')\
        .setCounterpartyType('PrivatePerson')\
        .setFirstName('Пилипко')\
        .setLastName('Петя')\
        .setMiddleName('Сергеевич')\
        .setPhone('+380661122333')\
        .setEmail('test2@i.ua')

    return counterparty.update()

def update2():
    counterparty = Counterparty()
    counterparty.setCityRef('8d5a980d-391c-11dd-90d9-001a92567626')\
        .setCounterpartyType('Organization')\
        .setEDRPOU('00000000')

    return counterparty.updateThirdPerson()

def delete():
    counterparty = Counterparty()
    counterparty.setRef('eb863d12-ac7d-11e4-a77a-005056887b8d')

    return counterparty.delete()

def getCounterparties():
    data = Counterparty_getCounterparties()
    data.setCounterpartyProperty('Recipient')
    data.setPage(1)
    data.setCityRef('8d5a980d-391c-11dd-90d9-001a92567626')
    data.setFindByString('Петр')
    # или
    # data.setRef('adcad698-011c-11e5-ad08-005056801333')

    return Counterparty.getCounterparties(data)

def getCounterparties2():
    data = MethodParameters()
    data.CounterpartyProperty = 'Recipient'
    data.Page = 1
    data.CityRef = '8d5a980d-391c-11dd-90d9-001a92567626'
    data.FindByString = 'Петр'

    return Counterparty.getCounterparties(data)

def getCounterpartyAddresses():
    data = Counterparty_getCounterpartyAddresses()
    data.setRef('512c13ac-1d43-11e4-acce-0050568002cf')

    return Counterparty.getCounterpartyAddresses(data)

def getCounterpartyContactPersons():
    data = Counterparty_getCounterpartyContactPersons()
    data.setRef('512c13ac-1d43-11e4-acce-0050568002cf')
    data.setPage('1')

    return Counterparty.getCounterpartyContactPersons(data)

def getCounterpartyOptions():
    data = Counterparty_getCounterpartyOptions()
    data.setRef('512c13ac-1d43-11e4-acce-0050568002cf')

    return Counterparty.getCounterpartyOptions(data)

def getCounterpartyByEDRPOU():
    data = Counterparty_getCounterpartyByEDRPOU()
    data.setEDRPOU('0000000')
    data.setCityRef('db5c88d0-391c-11dd-90d9-001a92567626')

    return Counterparty.getCounterpartyByEDRPOU(data)

def cloneLoyaltyCounterpartySender():
    data = Counterparty_cloneLoyaltyCounterpartySender()
    data.setCityRef('db5c88e0-391c-11dd-90d9-001a92567626')

    return Counterparty.cloneLoyaltyCounterpartySender(data)