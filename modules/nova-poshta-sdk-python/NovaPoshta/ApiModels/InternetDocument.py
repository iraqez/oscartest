

from NovaPoshta.Core.ApiModel import ApiModel


class InternetDocument(ApiModel):
    """
    InternetDocument - Модель для оформления отправлений
    """
        
    # Печать в формате PDF
    PRINT_TYPE_PDF = 'Pdf'
    # Печать в формате HTML
    PRINT_TYPE_HTML = 'Html'
    # Печатать 2 экземпляра
    PRINT_COPIES_DOUBLE = 'double'
    # Печатать 4 экземпляра
    PRINT_COPIES_FOURFOLD = 'fourfold'

    def __getDataInternetDocument(self):
        data = {}

        for key in self.__dict__:
            attr = getattr(self, key)
            if key == 'Sender':
                data['CitySender'] = attr.getCity()
                data['Sender'] = attr.getRef()
                data['SenderAddress'] = attr.getAddress()
                data['ContactSender'] = attr.getContact()
                data['SendersPhone'] = attr.getPhone()
            elif key == 'Recipient':
                data['CityRecipient'] = attr.getCity()
                data['Recipient'] = attr.getRef()
                data['RecipientAddress'] = attr.getAddress()
                data['ContactRecipient'] = attr.getContact()
                data['RecipientsPhone'] = attr.getPhone()
            else:
                data[key] = attr
        
        return data

    def setRef(self, value):
        """
        Устанавливает реф документа

        :param value: str
        :return: self
        """
        
        self.Ref = value
        return self

    def getRef(self):
        """
        Возвращает реф документа

        :return: str
        """
        
        return self.Ref

    def setSender(self, counterparty):
        """
        Устанавливает отправителя

        :param counterparty: NovaPoshta.Models.CounterpartyContact.CounterpartyContact
        :return: self
        """
        
        self.Sender = counterparty
        return self

    def getSender(self):
        """
        Возвращает отправителя
        
        :return: NovaPoshta.Models.CounterpartyContact.CounterpartyContact
        """
        
        return self.Sender

    def setRecipient(self, counterparty):
        """
        Устанавливает получателя

        :param counterparty: NovaPoshta.Models.CounterpartyContact.CounterpartyContact
        :return: self
        """
        
        self.Recipient = counterparty
        return self

    def getRecipient(self):
        """
        Возвращает получателя

        :return: NovaPoshta.Models.CounterpartyContact.CounterpartyContact
        """
        
        return self.Recipient

    def setThirdPerson(self, counterparty):
        """
        Устанавливает третье лицо

        :param counterparty: NovaPoshta.Models.CounterpartyContact.CounterpartyContact
        :return: self
        """
        
        self.ThirdPerson = counterparty
        return self

    def getThirdPerson(self):
        """
        Возвращает третье лицо

        :return: NovaPoshta.Models.CounterpartyContact.CounterpartyContact
        """
        
        return self.ThirdPerson

    def setDateTime(self, value):
        """
        Устанавливает дата создания

        :param value: str
        :return: self
        """
        
        self.DateTime = value
        return self

    def getDateTime(self):
        """
        Возвращает дата создания

        :return: str
        """
        
        return self.DateTime

    def setServiceType(self, value):
        """
        Устанавливает технологию доставки

        :param value: str
        :return: self
        """
        
        self.ServiceType = value
        return self

    def getServiceType(self):
        """
        Возвращает технологию доставки

        :return: str
        """
        
        return self.ServiceType

    def setPaymentMethod(self, value):
        """
        Устанавливает форму оплаты

        :param value: str
        :return: self
        """
        
        self.PaymentMethod = value
        return self

    def getPaymentMethod(self):
        """
        Возвращает форму оплаты

        :return: str
        """
        
        return self.PaymentMethod

    def setPayerType(self, value):
        """
        Устанавливает тип плательщика обратной доставки

        :param value: str
        :return: self
        """
        
        self.PayerType = value
        return self

    def getPayerType(self):
        """
        Возвращает тип плательщика обратной доставки

        :return: str
        """
        
        return self.PayerType

    def setCost(self, value):
        """
        Устанавливает объявленную стоимость

        :param value: float
        :return: self
        """
        
        self.Cost = value
        return self

    def getCost(self):
        """
        Возвращает объявленную стоимость

        :return: float
        """
        
        return self.Cost

    def setSeatsAmount(self, value):
        """
        Устанавливает количество мест отправления

        :param value: int
        :return: self
        """
        
        self.SeatsAmount = value
        return self

    def getSeatsAmount(self):
        """
        Возвращает количество мест отправления

        :return: int
        """
        
        return self.SeatsAmount

    def setDescription(self, value):
        """
        Устанавливает описания груза

        :param value: str
        :return: self
        """
        
        self.Description = value
        return self

    def getDescription(self):
        """
        Возвращает описания груза

        :return: str
        """
        
        return self.Description

    def setCargoType(self, value):
        """
        Устанавливает вид обратной доставки

        :param value: str
        :return: self
        """
        
        self.CargoType = value
        return self

    def getCargoType(self):
        """
        Возвращает вид обратной доставки

        :return: str
        """
        
        return self.CargoType

    def setWeight(self, value):
        """
        Устанавливает вес фактический, кг

        :param value: float
        :return: self
        """
        
        self.Weight = value
        return self

    def getWeight(self):
        """
        Возвращает вес фактический, кг

        :return: float
        """
        
        return self.Weight

    def setVolumeWeight(self, value):
        """
        Устанавливает вес объемный, кг

        :param value: float
        :return: self
        """
        
        self.VolumeWeight = value
        return self

    def getVolumeWeight(self):
        """
        Возвращает вес объемный, кг

        :return: float
        """
        
        return self.VolumeWeight

    def setVolumeGeneral(self, value):
        """
        Устанавливает объем общий, м.куб

        :param value: float
        :return: self
        """
        
        self.VolumeGeneral = value
        return self

    def getVolumeGeneral(self):
        """
        Возвращает объем общий, м.куб

        :return: float
        """
        
        return self.VolumeGeneral

    def setPack(self, value):
        """
        Устанавливает вид упаковки

        :param value: str
        :return: self
        """
        
        self.Pack = value
        return self

    def getPack(self):
        """
        Возвращает вид упаковки

        :return: str
        """
        
        return self.Pack

    def setAdditionalInformation(self, value):
        """
        Устанавливает дополнительную информацию об отправлении (любая, необходимая Клиенту информация в ЭН)

        :param value: str
        :return: self
        """
        
        self.AdditionalInformation = value
        return self

    def getAdditionalInformation(self):
        """
        Возвращает дополнительную информацию об отправлении (любая, необходимая Клиенту информация в ЭН)

        :return: str
        """
        
        return self.AdditionalInformation

    def setPackingNumber(self, value):
        """
        Устанавливает № упаковки

        :param value: str
        :return: self
        """
        
        self.PackingNumber = value
        return self

    def getPackingNumber(self):
        """
        Возвращает № упаковки

        :return: str
        """
        
        return self.PackingNumber

    def setInfoRegClientBarcodes(self, value):
        """
        Устанавливает номер внутреннего заказа Клиента (не хранится в ИС "Новая Почта")

        :param value: str
        :return: self
        """
        
        self.InfoRegClientBarcodes = value
        return self

    def getInfoRegClientBarcodes(self):
        """
        Возвращает номер внутреннего заказа Клиента (не хранится в ИС "Новая Почта")

        :return: str
        """
        
        return self.InfoRegClientBarcodes

    def setSaturdayDelivery(self, value):
        """
        Устанавливает субботнюю доставку

        :param value: str
        :return: self
        """
        
        self.SaturdayDelivery = value
        return self

    def getSaturdayDelivery(self):
        """
        Возвращает субботнюю доставку

        :return: str
        """
        
        return self.SaturdayDelivery

    def setSameDayDelivery(self, value):
        """
        Устанавливает день-в-день

        :param value: str
        :return: self
        """
        
        self.SameDayDelivery = value
        return self

    def getSameDayDelivery(self):
        """
        Возвращает день-в-день

        :return: str
        """
        
        return self.SameDayDelivery

    def setForwardingCount(self, value):
        """
        Устанавливает экспедирование

        :param value: str
        :return: self
        """
        
        self.ForwardingCount = value
        return self

    def getForwardingCount(self):
        """
        Возвращает экспедирование

        :return: str
        """
        
        return self.ForwardingCount

    def setIsTakeAttorney(self, value):
        """
        Устанавливает забор доверенности

        :param value: bool
        :return: self
        """
        
        self.IsTakeAttorney = value
        return self

    def getIsTakeAttorney(self):
        """
        Возвращает забор доверенности

        :return: bool
        """
        
        return self.IsTakeAttorney

    def setPreferredDeliveryDate(self, value):
        """
        Устанавливает желаемаую дату доставки

        :param value: str
        :return: self
        """
        
        self.PreferredDeliveryDate = value
        return self

    def getPreferredDeliveryDate(self):
        """
        Возвращает желаемаую дату доставки

        :return: str
        """
        
        return self.PreferredDeliveryDate

    def setTimeInterval(self, value):
        """
        Устанавливает доставку временных интервалов

        :param value: str
        :return: self
        """
        
        self.TimeInterval = value
        return self

    def getTimeInterval(self):
        """
        Возвращает доставку временных интервалов

        :return: str
        """
        
        return self.TimeInterval

    def addCargoDetail(self, value):
        """
        Добавляет параметры груза

        :param value: NovaPoshta.Models.Cargo.Cargo
        :return: self
        """
        
        if self.CargoDetails is None:
            self.CargoDetails = []
        self.CargoDetails.append(value)
        return self

    def getCargoDetails(self):
        """
        Возвращает параметры груза

        :return: list
        """
        
        if self.CargoDetails is None:
            self.CargoDetails = []
        return self.CargoDetails

    def clearCargoDetails(self):
        """
        Очищает параметры груза

        :return: list
        """
        
        self.CargoDetails = []
        return self

    def addOptionsSeat(self, value):
        """
        Добавляет параметры места

        :param value: NovaPoshta.Models.OptionsSeat.OptionsSeat
        :return: self
        """
        
        if self.OptionsSeat is None:
            self.OptionsSeat = []
        self.OptionsSeat.append(value)
        return self

    def getOptionsSeats(self):
        """
        Возвращает параметры мест

        :return: list
        """
        
        if self.OptionsSeat is None:
            self.OptionsSeat = []
        return self.OptionsSeat

    def clearOptionsSeat(self):
        """
        Очищает параметры мест

        :return: self
        """
        
        self.OptionsSeat = []
        return self

    def addBackwardDeliveryData(self, value):
        """
        Добавляет обратную доставку

        :param value: NovaPoshta.Models.BackwardDeliveryData.BackwardDeliveryData
        :return: self
        """
        
        if self.BackwardDeliveryData is None:
            self.BackwardDeliveryData = []
        self.BackwardDeliveryData.append(value)
        return self

    def getBackwardDeliveryData(self):
        """
        Возвращает обратную доставку

        :return: list
        """
        
        if self.BackwardDeliveryData is None:
            self.BackwardDeliveryData = []
        return self.BackwardDeliveryData

    def clearBackwardDeliveryData(self):
        """
        Очищает  обратную доставку

        :return: self
        """
        
        self.BackwardDeliveryData = []
        return self

    def setNumberOfFloorsLifting(self, value):
        """
        Устанавливает подъем на этаж

        :param value: int
        :return: self
        """
        
        self.NumberOfFloorsLifting = value
        return self

    def getNumberOfFloorsLifting(self):
        """
        Устанавливает подъем на этаж

        :return: int
        """
        
        return self.NumberOfFloorsLifting

    def setAccompanyingDocuments(self, value):
        """
        Устанавливает сопровождающие документы

        :param value: str
        :return: self
        """
        
        self.AccompanyingDocuments = value
        return self

    def getAccompanyingDocuments(self):
        """
        Возвращает сопровождающие документы
           @return str
        """
        
        return self.AccompanyingDocuments

    def save(self):
        """
        Вызвать метод save() - создание ЭН

        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return self._sendData('save', self.__getDataInternetDocument())

    def update(self):
        """
        Вызвать метод update() - редактирование ЭН

        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return self._sendData('update', self.__getDataInternetDocument())

    def delete(self):
        """
        Вызвать метод delete() - удаление документа

        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return self._sendData('delete', self.__getDataInternetDocument())

    @staticmethod
    def getDocumentDeliveryDate(data=None):
        """
        Вызвать метод getDocumentDeliveryDate() - ориентировочная дата доставки

        :type data: NovaPoshta.MethodParameters.MethodParameters.MethodParameters
        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return ApiModel._sendData(InternetDocument, 'getDocumentDeliveryDate', data)

    @staticmethod
    def getDocument(data=None):
        """
        Вызвать метод getDocument() - получить ЭН

        :type data: NovaPoshta.MethodParameters.MethodParameters.MethodParameters
        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return ApiModel._sendData(InternetDocument, 'getDocument', data)

    @staticmethod
    def getDocumentList(data=None):
        """
        Вызвать метод getDocumentList() - получает список ЭН

        :type data: NovaPoshta.MethodParameters.MethodParameters.MethodParameters
        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return ApiModel._sendData(InternetDocument, 'getDocumentList', data)

    @staticmethod
    def printDocument(data=None):
        """
        Вызвать метод printDocument() - печать ЭН

        :type data: NovaPoshta.MethodParameters.MethodParameters.MethodParameters
        :return: str
        """
        
        return ApiModel._sendData(InternetDocument, 'printDocument', data)

    @staticmethod
    def printMarkings(data=None):
        """
        Вызвать метод printMarkings() - печать маркировок

        :type data: NovaPoshta.MethodParameters.MethodParameters.MethodParameters
        :return: str
        """
        
        return ApiModel._sendData(InternetDocument, 'printMarkings', data)

    @staticmethod
    def documentsTracking(data=None):
        """
        Вызвать метод documentsTracking() - трекинг документов

        :type data: NovaPoshta.MethodParameters.MethodParameters.MethodParameters
        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return ApiModel._sendData(InternetDocument, 'documentsTracking', data)

    @staticmethod
    def getDocumentPrice(data=None):
        """
        Вызвать метод getDocumentPrice() - расчет стоимости доставки

        :type data: NovaPoshta.MethodParameters.MethodParameters.MethodParameters
        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return ApiModel._sendData(InternetDocument, 'getDocumentPrice', data)

    def __getPrintLink(typePrint, data=None):
        pass
