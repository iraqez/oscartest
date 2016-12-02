

from NovaPoshta.Core.ApiModel import ApiModel

class Counterparty(ApiModel):
    """
    Counterparty - Модель для работы с данными контрагента
    """
        
    # Третье лицо
    THIRD_PERSON = 'ThirdPerson'

    def save(self):
        """
        Вызвать метод save() - сохранить контрагента

        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return self._sendData('save', self)

    def update(self):
        """
        Вызвать метод update() - обновить данные контрагента

        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return self._sendData('update', self)

    def saveThirdPerson(self):
        """
        Вызвать метод saveThirdPerson() - сохранить контрагента с типом "третье лицо" Функция
        доступна для клиентов, заключивших договор с компанией "Новая Почта"

        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        self.setCounterpartyProperty(Counterparty.THIRD_PERSON)

        return self._sendData('saveThirdPerson', self)

    def updateThirdPerson(self):
        """
        Вызвать метод updateThirdPerson() - обновить данные контрагента с типом "третье лицо" Функция
        доступна для клиентов, заключивших договор с компанией "Новая Почта"

        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        self.setCounterpartyProperty(Counterparty.THIRD_PERSON)

        return self._sendData('updateThirdPerson', self)

    def delete(self):
        """
        Вызвать метод delete() - удалить контрагента отправителя/получателя

        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return self._sendData('delete', self)

    def setRef(self, value):
        """
        Устанавливает реф

        :param value: str
        :return: self
        """
        
        self.Ref = value
        return self

    def getRef(self):
        """
        Возвращает реф

        :return: str
        """
        
        return self.Ref

    def setCounterpartyProperty(self, value):
        """
        Устанавливает свойство контрагента

        :param value: str
        :return: self
        """
        
        self.CounterpartyProperty = value
        return self

    def getCounterpartyProperty(self):
        """
        Возвращает свойство контрагента

        :return: str
        """
        
        return self.CounterpartyProperty

    def setCityRef(self, value):
        """
        Устанавливает реф города

        :param value: str
        :return: self
        """
        
        self.CityRef = value
        return self

    def getCityRef(self):
        """
        Возвращает реф города

        :return: str
        """
        
        return self.CityRef

    def setCounterpartyType(self, value):
        """
        Устанавливает тип контрагента

        :param value: str
        :return: self
        """
        
        self.CounterpartyType = value
        return self

    def getCounterpartyType(self):
        """
        Возвращает тип контрагента

        :return: str
        """
        
        return self.CounterpartyType

    def setFirstName(self, value):
        """
        Устанавливает фамилию

        :param value: str
        :return: self
        """
        
        self.FirstName = value
        return self

    def getFirstName(self):
        """
        Возвращает фамилию

        :return: str
        """
        
        return self.FirstName

    def setMiddleName(self, value):
        """
        Устанавливает отчество

        :param value: str
        :return: self
        """
        
        self.MiddleName = value
        return self

    def getMiddleName(self):
        """
        Возвращает отчество

        :return: str
        """
        
        return self.MiddleName

    def setLastName(self, value):
        """
        Устанавливает имя

        :param value: str
        :return: self
        """
        
        self.LastName = value
        return self

    def getLastName(self):
        """
        Возвращает имя

        :return: str
        """
        
        return self.LastName

    def setPhone(self, value):
        """
        Устанавливает номер телефона

        :param value: str
        :return: self
        """
        
        self.Phone = value
        return self

    def getPhone(self):
        """
        Возвращает номер телефона

        :return: str
        """
        
        return self.Phone

    def setEmail(self, value):
        """
        Устанавливает email

        :param value: str
        :return: self
        """
        
        self.Email = value
        return self

    def getEmail(self):
        """
        Возвращает email

        :return: str
        """
        
        return self.Email

    def setEDRPOU(self, value):
        """
        Устанавливает ОКПО

        :param value: str
        :return: self
        """
        
        self.EDRPOU = value
        return self

    def getEDRPOU(self):
        """
        Возвращает ОКПО

        :return: str
        """
        
        return self.EDRPOU

    def setOwnershipForm(self, value):
        """
        Устанавливает форму собственности

        :param value: str
        :return: self
        """
        
        self.OwnershipForm = value
        return self

    def getOwnershipForm(self):
        """
        Возвращает форму собственности

        :return: str
        """
        
        return self.OwnershipForm

    @staticmethod
    def cloneLoyaltyCounterpartySender(data = None):
        """
        Вызвать метод cloneLoyaltyCounterpartySender() - создать контрагента-отправителя в выбранном
        городе (для участников программы лояльности)  Метод: cloneLoyaltyCounterpartySender —
        создает контрагента-отправителя, если выбранный город-отправитель отличается от
        города в котором зарегистрирован пользователь

        :type data: NovaPoshta.MethodParameters.MethodParameters.MethodParameters
        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return Counterparty._sendData(Counterparty, 'cloneLoyaltyCounterpartySender', data)

    @staticmethod
    def getCounterparties(data = None):
        """
        Вызвать метод getCounterparties() - загрузить список контрагентов отправителей/получателей

        :type data: NovaPoshta.MethodParameters.MethodParameters.MethodParameters
        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return Counterparty._sendData(Counterparty, 'getCounterparties', data)

    @staticmethod
    def getCounterpartyAddresses(data = None):
        """
        Вызвать метод getCounterpartyAddresses() - загрузить список адресов контрагентов

        :type data: NovaPoshta.MethodParameters.MethodParameters.MethodParameters
        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return Counterparty._sendData(Counterparty, 'getCounterpartyAddresses', data)

    @staticmethod
    def getCounterpartyContactPersons(data = None):
        """
        Вызвать метод getCounterpartyContactPersons() - загрузить список контактных лиц контрагента

        :type data: NovaPoshta.MethodParameters.MethodParameters.MethodParameters
        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return Counterparty._sendData(Counterparty, 'getCounterpartyContactPersons', data)

    @staticmethod
    def getCounterpartyByEDRPOU(data = None):
        """
        Вызвать метод getCounterpartyByEDRPOU() - найти контрагента по коду ОКПО

        :type data: NovaPoshta.MethodParameters.MethodParameters.MethodParameters
        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return Counterparty._sendData(Counterparty, 'getCounterpartyByEDRPOU', data)

    @staticmethod
    def getCounterpartyOptions(data = None):
        """
        Вызвать метод getCounterpartyOptions() - загрузить параметры контрагента

        :type data: NovaPoshta.MethodParameters.MethodParameters.MethodParameters
        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return Counterparty._sendData(Counterparty, 'getCounterpartyOptions', data)