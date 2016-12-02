from NovaPoshta.MethodParameters.Common_getCargoDescriptionList import Common_getCargoDescriptionList
from NovaPoshta.MethodParameters.Common_getTimeIntervals import Common_getTimeIntervals
from NovaPoshta.ApiModels.Common import Common

__author__ = 'user'


def getBackwardDeliveryCargoTypes():
    return Common.getBackwardDeliveryCargoTypes()

def getCargoDescriptionList():
    data = Common_getCargoDescriptionList()
    data.setPage(1).setFindByString("Шин")

    return Common.getCargoDescriptionList(data)

def getCargoTypes():
    return Common.getCargoTypes()

def getDocumentStatuses():
    return Common.getDocumentStatuses()

def getOwnershipFormsList():
    return Common.getOwnershipFormsList()

def getPalletsList():
    return Common.getPalletsList()

def getPaymentForms():
    return Common.getPaymentForms()

def getServiceTypes():
    return Common.getServiceTypes()

def getTimeIntervals():
    data = Common_getTimeIntervals()
    data.setRecipientCityRef('8d5a980d-391c-11dd-90d9-001a92567626')\
        .setDateTime('15.09.2015')

    return Common.getTimeIntervals(data)

def getTiresWheelsList():
    return Common.getTiresWheelsList()

def getTraysList():
    return Common.getTraysList()

def getTypesOfCounterparties():
    return Common.getTypesOfCounterparties()

def getTypesOfPayers():
    return Common.getTypesOfPayers()

def getTypesOfPayersForRedelivery():
    return Common.getTypesOfPayersForRedelivery()