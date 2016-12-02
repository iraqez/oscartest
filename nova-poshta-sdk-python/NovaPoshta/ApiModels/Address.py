
from NovaPoshta.Core.ApiModel import ApiModel

class Address(ApiModel):
    """
    Модель для работы с адресами  Class Address
    """

    def save(self):
        """
        Вызвать метод save() - создать адрес отправителя/получателя

        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        return self._sendData('save', self)

    def update(self):
        """
        Вызвать метод update() - редактировать адрес отправителя/получателя

        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        return self._sendData('update', self)

    def delete(self):
        """
        Вызвать метод delete() - удалить ранее созданный адрес

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

    def setCounterpartyRef(self, value):
        """
        Устанавливает реф контрагента

        :param value: str
        :return: self
        """
        self.CounterpartyRef = value
        return self

    def getCounterpartyRef(self):
        """
        Возвращает реф контрагента

        :return: str
        """
        return self.CounterpartyRef

    def setStreetRef(self, value):
        """
        Устанавливает реф улицы

        :param value: str
        :return: self
        """
        self.StreetRef = value
        return self

    def getStreetRef(self):
        """
        Возвращает реф улицы

        :return: str
        """
        return self.StreetRef

    def setBuildingNumber(self, value):
        """
        Устанавливает номер дома

        :param value: str
        :return: self
        """
        self.BuildingNumber = value
        return self

    def getBuildingNumber(self):
        """
        Возвращает номер дома

        :return: str
        """
        return self.BuildingNumber

    def setFlat(self, value):
        """
        Устанавливает номер квартиры

        :param value: str
        :return: self
        """
        self.Flat = value
        return self

    def getFlat(self):
        """
        Возвращает номер квартиры

        :return: str
        """
        return self.Flat

    def setNote(self, value):
        """
        Устанавливает комментарий

        :param value: str
        :return: self
        """
        self.Note = value
        return self

    def getNote(self):
        """
        Возвращает комментарий

        :return: str
        """
        return self.Note

    def setBuildingRef(self, value):
        """
        Устанавливает реф дома

        :param value: str
        :return: self
        """
        self.BuildingRef = value
        return self

    def getBuildingRef(self):
        """
        Возвращает реф дома

        :return: str
        """
        return self.BuildingRef

    @staticmethod
    def getCities(data = None):
        """
        Вызвать метод getCities() - загрузить справочник городов компании «Новая Почта»

        :type data: NovaPoshta.MethodParameters.MethodParameters.MethodParameters
        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        return ApiModel._sendData(Address, 'getCities', data)

    @staticmethod
    def getStreet(data = None):
        """
        Вызвать метод getStreet() - загрузить справочник улиц компании «Новая Почта»

        :type data: NovaPoshta.MethodParameters.MethodParameters.MethodParameters
        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        return ApiModel._sendData(Address, 'getStreet', data)

    def getWarehouses(data = None):
        """
        Вызвать метод getWarehouses() - загрузить справочник отделений компании «Новая Почта»

        :type data: NovaPoshta.MethodParameters.MethodParameters.MethodParameters
        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        return ApiModel._sendData(Address, 'getWarehouses')

    @staticmethod
    def getAreas(data = None):
        """
        Вызвать метод getAreas() - загрузить справочник географических областей Украины

        :type data: NovaPoshta.MethodParameters.MethodParameters.MethodParameters
        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        return ApiModel._sendData(Address, 'getAreas', data)