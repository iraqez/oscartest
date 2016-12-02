from NovaPoshta.ApiModels.ContactPerson import ContactPerson

__author__ = 'user'

def save():
    contactPerson = ContactPerson()
    contactPerson.setCounterpartyRef('2718756a-b39b-11e4-a77a-005056887b8d')\
        .setFirstName('Пандан')\
        .setLastName('Джедай')\
        .setMiddleName('Джедаевич')\
        .setPhone('380660000000')\
        .setEmail('test@i.ua')

    return contactPerson.save()

def update():
    contactPerson = ContactPerson()
    contactPerson.setRef('6ba7314c-b543-11e4-a77a-005056887b8d')\
        .setCounterpartyRef('2718756a-b39b-11e4-a77a-005056887b8d')\
        .setFirstName('Панданюк')\
        .setLastName('Джедай')\
        .setMiddleName('Джедаевич')\
        .setPhone('380660000000')\
        .setEmail('test2@i.ua')

    return contactPerson.update()

def delete():
    contactPerson = ContactPerson()
    contactPerson.setRef('6ba7314c-b543-11e4-a77a-005056887b8d')

    return contactPerson.delete()