from NovaPoshta.ApiModels.Address import Address
from NovaPoshta.MethodParameters.Address_getAreas import Address_getAreas
from NovaPoshta.MethodParameters.Address_getCities import Address_getCities
from NovaPoshta.MethodParameters.Address_getStreet import Address_getStreet
from NovaPoshta.MethodParameters.Address_getWarehouses import Address_getWarehouses

__author__ = 'user'

def save():
    address = Address()
    address.setCounterpartyRef('2718756a-b39b-11e4-a77a-005056887b8d')\
        .setBuildingNumber('2/2')\
        .setFlat('22')\
        .setNote('Первый подъезд')\
        .setStreetRef('c55c9056-4148-11dd-9198-001d60451983')

    return address.save()

def update():
    address = Address()
    address.setRef('e29115c8-6f59-11e4-acce-0050568002cf')\
        .setCounterpartyRef('2718756a-b39b-11e4-a77a-005056887b8d')\
        .setBuildingNumber('92')\
        .setFlat('22')\
        .setNote('Первый')\
        .setStreetRef('c55c9056-4148-11dd-9198-001d60451983')

    return address.update()

def delete():
    address = Address()
    address.setRef('e29115c8-6f59-11e4-acce-0050568002cf')

    return address.delete()

def getCities():
    data = Address_getCities()
    data.setRef('db5c896a-391c-11dd-90d9-001a92567626')\
        .setPage(1)\
        .setFindByString('Пол')

    return Address.getCities(data)

def getStreet():
    data = Address_getStreet()
    data.setCityRef('8d5a980d-391c-11dd-90d9-001a92567626')\
        .setFindByString('Авт')\
        .setPage(1)

    return Address.getStreet(data)

def getWarehouses():
    data = Address_getWarehouses()
    data.setCityRef('ebc0eda9-93ec-11e3-b441-0050568002cf')\
        .setPage(1)

    return Address.getWarehouses(data)

def getAreas():
    data = Address_getAreas()
    data.setRef('7150813d-9b87-11de-822f-000c2965ae0e')\
        .setPage(1)

    return Address.getAreas(data)
