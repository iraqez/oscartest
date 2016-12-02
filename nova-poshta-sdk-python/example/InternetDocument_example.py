from NovaPoshta.ApiModels.InternetDocument import InternetDocument
from NovaPoshta.MethodParameters.InternetDocument_documentsTracking import InternetDocument_documentsTracking
from NovaPoshta.MethodParameters.InternetDocument_getDocumentDeliveryDate import \
    InternetDocument_getDocumentDeliveryDate
from NovaPoshta.MethodParameters.InternetDocument_getDocumentList import InternetDocument_getDocumentList
from NovaPoshta.MethodParameters.InternetDocument_getDocument import InternetDocument_getDocument
from NovaPoshta.MethodParameters.InternetDocument_getDocumentPrice import InternetDocument_getDocumentPrice
from NovaPoshta.Models.BackwardDeliveryData import BackwardDeliveryData
from NovaPoshta.Models.Cargo import Cargo
from NovaPoshta.Models.CounterpartyContact import CounterpartyContact
from NovaPoshta.Models.OptionsSeat import OptionsSeat

__author__ = 'user'

def save():
    sender = CounterpartyContact()
    sender.setCity('8d5a980d-391c-11dd-90d9-001a92567626')
    sender.setRef('f867c762-e66a-11e3-8c4a-0050568002cf')
    sender.setAddress('1ec09d88-e1c2-11e3-8c4a-0050568002cf')
    sender.setContact('e23f313c-e67a-11e3-8c4a-0050568002cf')
    sender.setPhone('+380660000000')

    recipient = CounterpartyContact()
    recipient.setCity('db5c88de-391c-11dd-90d9-001a92567626')
    recipient.setRef('7da56a9c-f205-11e3-8c4a-0050568002cf')
    recipient.setAddress('daec7561-b457-11e4-a77a-005056887b8d')
    recipient.setContact('57065334-f211-11e3-8c4a-0050568002cf')
    recipient.setPhone('+380660000001')

    backwardDeliveryData1 = BackwardDeliveryData()
    backwardDeliveryData1.setPayerType('Recipient')
    backwardDeliveryData1.setCargoType('Money')
    backwardDeliveryData1.setRedeliveryString('452')

    backwardDeliveryData2 = BackwardDeliveryData()
    backwardDeliveryData2.setPayerType('Recipient')
    backwardDeliveryData2.setCargoType('Documents')
    backwardDeliveryData2.setRedeliveryString('Тех. документация')

    internetDocument = InternetDocument()
    internetDocument.setSender(sender)
    internetDocument.setRecipient(recipient)
    internetDocument.setServiceType('WarehouseDoors')
    internetDocument.setPayerType('Recipient')
    internetDocument.setPaymentMethod('Cash')
    internetDocument.setCargoType('Cargo')
    internetDocument.setWeight('31')
    internetDocument.setVolumeGeneral('0.002')
    internetDocument.setSeatsAmount('2')
    internetDocument.setCost('2')
    internetDocument.setDescription(' fd  fsf2')
    internetDocument.setDateTime('10.08.2015')
    internetDocument.setPreferredDeliveryDate('20.08.2015')
    internetDocument.setTimeInterval('CityDeliveryTimeInterval2')
    internetDocument.setPackingNumber('55')
    internetDocument.setInfoRegClientBarcodes('55552')
    internetDocument.setSaturdayDelivery('true')
    internetDocument.setNumberOfFloorsLifting('12')
    internetDocument.setAccompanyingDocuments('Большая корзина')
    internetDocument.setAdditionalInformation('Стекло')
    internetDocument.addBackwardDeliveryData(backwardDeliveryData1)
    internetDocument.addBackwardDeliveryData(backwardDeliveryData2)

    return internetDocument.save()

def save_2():
    sender = CounterpartyContact()
    sender.setCity('8d5a980d-391c-11dd-90d9-001a92567626')\
        .setRef('f867c762-e66a-11e3-8c4a-0050568002cf')\
        .setAddress('1ec09d88-e1c2-11e3-8c4a-0050568002cf')\
        .setContact('e23f313c-e67a-11e3-8c4a-0050568002cf')\
        .setPhone('+380660000000')

    recipient = CounterpartyContact()
    recipient.setCity('db5c88de-391c-11dd-90d9-001a92567626')\
        .setRef('7da56a9c-f205-11e3-8c4a-0050568002cf')\
        .setAddress('daec7561-b457-11e4-a77a-005056887b8d')\
        .setContact('57065334-f211-11e3-8c4a-0050568002cf')\
        .setPhone('+380660000001')

    backwardDeliveryData1 = BackwardDeliveryData()
    backwardDeliveryData1.setPayerType('Sender')\
        .setCargoType('Other')\
        .setRedeliveryString('Чемодан')

    trayCargoA = Cargo()
    trayCargoA.setAmount(3)\
        .setCargoDescription('d5c36c5d-a29d-11de-a2ca-000c294065a1')

    trayCargoE = Cargo()
    trayCargoE.setAmount(1)\
        .setCargoDescription('d5c36c5c-a29d-11de-a2ca-000c294065a1')

    backwardDeliveryData2 = BackwardDeliveryData()
    backwardDeliveryData2.setPayerType('Sender')\
        .setCargoType('Trays')\
        .setRedeliveryString('Поддони( тара )')\
        .addTray(trayCargoA)\
        .addTray(trayCargoE)

    internetDocument = InternetDocument()
    internetDocument.setSender(sender)\
        .setRecipient(recipient)\
        .setServiceType('WarehouseDoors')\
        .setPayerType('Recipient')\
        .setPaymentMethod('Cash')\
        .setCargoType('Documents')\
        .setWeight('0.5')\
        .setSeatsAmount('1')\
        .setCost('200')\
        .setDescription('ТЦ')\
        .addBackwardDeliveryData(backwardDeliveryData2)\
        .addBackwardDeliveryData(backwardDeliveryData1)

    return internetDocument.save()

def save_3():
    sender = CounterpartyContact()
    sender.setCity('8d5a980d-391c-11dd-90d9-001a92567626')\
        .setRef('f867c762-e66a-11e3-8c4a-0050568002cf')\
        .setAddress('1ec09d88-e1c2-11e3-8c4a-0050568002cf')\
        .setContact('e23f313c-e67a-11e3-8c4a-0050568002cf')\
        .setPhone('+380660000000')

    recipient = CounterpartyContact()
    recipient.setCity('db5c88de-391c-11dd-90d9-001a92567626')\
        .setRef('7da56a9c-f205-11e3-8c4a-0050568002cf')\
        .setAddress('daec7561-b457-11e4-a77a-005056887b8d')\
        .setContact('57065334-f211-11e3-8c4a-0050568002cf')\
        .setPhone('+380660000001')

    backwardDeliveryData = BackwardDeliveryData()
    backwardDeliveryData.setPayerType('Sender')\
        .setCargoType('Money')\
        .setRedeliveryString('500')

    optionsSeat1 = OptionsSeat()
    optionsSeat1.setVolumetricHeight(20)\
        .setVolumetricLength(20)\
        .setVolumetricWidth(20)\
        .setWeight(20)

    optionsSeat2 = OptionsSeat()
    optionsSeat2.setVolumetricHeight(15)\
        .setVolumetricLength(15)\
        .setVolumetricWidth(15)\
        .setWeight(15)

    optionsSeat3 = OptionsSeat()
    optionsSeat3.setVolumetricVolume(0.05)\
        .setWeight(10)

    optionsSeat4 = OptionsSeat()
    optionsSeat4.setVolumetricVolume(0.05)\
        .setWeight(15)

    internetDocument = InternetDocument()
    internetDocument.setSender(sender)\
        .setRecipient(recipient)\
        .setServiceType('WarehouseDoors')\
        .setPayerType('Recipient')\
        .setPaymentMethod('Cash')\
        .setCargoType('Cargo')\
        .setCost('200')\
        .setDescription('ТЦ')\
        .addOptionsSeat(optionsSeat1)\
        .addOptionsSeat(optionsSeat2)\
        .addOptionsSeat(optionsSeat3)\
        .addOptionsSeat(optionsSeat4)\
        .addBackwardDeliveryData(backwardDeliveryData)

    internetDocument.CargoType = 'Cargo'

    return internetDocument.save()

def save_4():
    sender = CounterpartyContact()
    sender.setCity('8d5a980d-391c-11dd-90d9-001a92567626')\
        .setRef('f867c762-e66a-11e3-8c4a-0050568002cf')\
        .setAddress('1ec09d88-e1c2-11e3-8c4a-0050568002cf')\
        .setContact('e23f313c-e67a-11e3-8c4a-0050568002cf')\
        .setPhone('+380660000000')

    recipient = CounterpartyContact()
    recipient.setCity('db5c88de-391c-11dd-90d9-001a92567626')\
        .setRef('7da56a9c-f205-11e3-8c4a-0050568002cf')\
        .setAddress('daec7561-b457-11e4-a77a-005056887b8d')\
        .setContact('57065334-f211-11e3-8c4a-0050568002cf')\
        .setPhone('+380660000001')

    optionsSeat1 = OptionsSeat()
    optionsSeat1.setVolumetricHeight(100)\
        .setVolumetricLength(100)\
        .setVolumetricWidth(100)\
        .setWeight(100)

    optionsSeat2 = OptionsSeat()
    optionsSeat2.setVolumetricHeight(100)\
        .setVolumetricLength(100)\
        .setVolumetricWidth(170)\
        .setWeight(550)

    internetDocument = InternetDocument()
    internetDocument.setSender(sender)\
        .setRecipient(recipient)\
        .setServiceType('WarehouseDoors')\
        .setPayerType('Recipient')\
        .setPaymentMethod('Cash')\
        .setCargoType('Pallet')\
        .setCost('200')\
        .setDescription('ТЦ')\
        .addOptionsSeat(optionsSeat1)\
        .addOptionsSeat(optionsSeat2)

    return internetDocument.save()

def save_5():
    sender = CounterpartyContact()
    sender.setCity('8d5a980d-391c-11dd-90d9-001a92567626')\
        .setRef('f867c762-e66a-11e3-8c4a-0050568002cf')\
        .setAddress('1ec09d88-e1c2-11e3-8c4a-0050568002cf')\
        .setContact('e23f313c-e67a-11e3-8c4a-0050568002cf')\
        .setPhone('+380660000000')

    recipient = CounterpartyContact()
    recipient.setCity('db5c88de-391c-11dd-90d9-001a92567626')\
        .setRef('7da56a9c-f205-11e3-8c4a-0050568002cf')\
        .setAddress('daec7561-b457-11e4-a77a-005056887b8d')\
        .setContact('57065334-f211-11e3-8c4a-0050568002cf')\
        .setPhone('+380660000001')

    tiresWheels1 = Cargo()
    tiresWheels1.setAmount(2)\
        .setCargoDescription('20f7b625-9add-11e3-b441-0050568002cf')

    tiresWheels2 = Cargo()
    tiresWheels2.setAmount(2)\
        .setCargoDescription('20f7b627-9add-11e3-b441-0050568002cf')

    tiresWheels3 = Cargo()
    tiresWheels3.setAmount(5)\
        .setCargoDescription('d7c456c6-aa8b-11e3-9fa0-0050568002cf')

    tiresWheels4 = Cargo()
    tiresWheels4.setAmount(1)\
        .setCargoDescription('d7c456ca-aa8b-11e3-9fa0-0050568002cf')

    internetDocument = InternetDocument()
    internetDocument.setSender(sender)\
        .setRecipient(recipient)\
        .setServiceType('WarehouseDoors')\
        .setPayerType('Recipient')\
        .setPaymentMethod('Cash')\
        .setCargoType('TiresWheels')\
        .setCost('200')\
        .setDescription('ТЦ')\
        .addCargoDetail(tiresWheels1)\
        .addCargoDetail(tiresWheels2)\
        .addCargoDetail(tiresWheels3)\
        .addCargoDetail(tiresWheels4)

    return internetDocument.save()

def update():
    sender = CounterpartyContact()
    sender.setCity('8d5a980d-391c-11dd-90d9-001a92567626')\
        .setRef('f867c762-e66a-11e3-8c4a-0050568002cf')\
        .setAddress('1ec09d88-e1c2-11e3-8c4a-0050568002cf')\
        .setContact('e23f313c-e67a-11e3-8c4a-0050568002cf')\
        .setPhone('+380660000000')

    recipient = CounterpartyContact()
    recipient.setCity('db5c88de-391c-11dd-90d9-001a92567626')\
        .setRef('7da56a9c-f205-11e3-8c4a-0050568002cf')\
        .setAddress('daec7561-b457-11e4-a77a-005056887b8d')\
        .setContact('57065334-f211-11e3-8c4a-0050568002cf')\
        .setPhone('+380660000001')

    internetDocument = InternetDocument()
    internetDocument.setRef('321be81e-3383-11e5-ad08-005056801333')\
        .setSender(sender)\
        .setRecipient(recipient)\
        .setServiceType('WarehouseDoors')\
        .setPayerType('Recipient')\
        .setPaymentMethod('Cash')\
        .setCargoType('Documents')\
        .setWeight('0.5')\
        .setSeatsAmount('1')\
        .setCost('200')\
        .setDescription('ТЦ')\
        .setDateTime('10.09.2015')

    return internetDocument.update()

def delete():
    internetDocument = InternetDocument()
    internetDocument.setRef('70ec0f63-bf6b-11e4-a77a-005056887b8d')

    return internetDocument.delete()

def getDocumentDeliveryDate():
    data = InternetDocument_getDocumentDeliveryDate()
    data.setDateTime('16.10.2015')
    data.setCitySender('8d5a980d-391c-11dd-90d9-001a92567626')
    data.setCityRecipient('db5c88de-391c-11dd-90d9-001a92567626')
    data.setServiceType('WarehouseDoors')

    return InternetDocument.getDocumentDeliveryDate(data)

def documentsTracking():
    refs = ['20400000310076', '20400000310077']

    data = InternetDocument_documentsTracking()
    data.setDocuments(refs)

     # или

    data.addDocument('20400000310076')
    data.addDocument('20400000310077')

    return InternetDocument.documentsTracking(data)

def getDocumentPrice():
    data = InternetDocument_getDocumentPrice()
    data.setCitySender('8d5a980d-391c-11dd-90d9-001a92567626')
    data.setCityRecipient('db5c88f0-391c-11dd-90d9-001a92567626')
    data.setWeight('10')
    data.setCost('200')
    data.setServiceType('DoorsDoors')
    data.setDateTime('15.10.2015')

    return InternetDocument.getDocumentPrice(data)

def printDocument():
    # todo доделать
    pass

def printMarkings():
    # todo доделать
    pass

def getDocument():
    data = InternetDocument_getDocument()
    data.setRef('e74cfc48-323e-11e5-ad08-005056801333')

    return InternetDocument.getDocument(data)

def getDocumentList():
    data = InternetDocument_getDocumentList()
    data.setIntDocNumber('20400000310107')

    return InternetDocument.getDocumentList(data)

def getDocumentList2():
    data = InternetDocument_getDocumentList()
    data.setInfoRegClientBarcodes('55552')

    return InternetDocument.getDocumentList(data)

def getDocumentList3():
    data = InternetDocument_getDocumentList()
    data.setDeliveryDateTime('20.03.2015')
    data.setRecipientDateTime('14.03.2015')
    data.setDeliveryDateTime('14.03.2015')
    data.setCreateTime('10.03.2015')
    data.setSenderRef('f867c762-e66a-11e3-8c4a-0050568002cf')
    data.setRecipientRef('7da56a9c-f205-11e3-8c4a-0050568002cf')
    data.setWeightFrom('5')
    data.setWeightTo('600')
    data.setCostFrom('5')
    data.setCostTo('15000')
    data.setSeatsAmountFrom('5')
    data.setSeatsAmountTo('15')
    data.setSeatsAmountFrom('5')
    data.setSeatsAmountTo('15')
    data.setCostOnSiteFrom('500')
    data.setCostOnSiteTo('1500')
    data.setDateTime('09.03.2015')
    #  константы для сортирования: InternetDocument_getDocumentList.ORDER_FIELD...
    data.setOrderField(InternetDocument_getDocumentList.ORDER_FIELD_Cost)
    data.setScanSheetRef('b107a458-c6fe-11e4-ac12-005056801333')
    data.setPage('1')
    data.setOrderDirection(InternetDocument_getDocumentList.ORDER_DIRECTION_ASC)
    data.setIsAfterpayment('true')

    return InternetDocument.getDocumentList(data)


def getDocumentList4():
    data = InternetDocument_getDocumentList()
    data.setDateTime('24.07.2015')
    data.setStateIds([1])

    return InternetDocument.getDocumentList(data)