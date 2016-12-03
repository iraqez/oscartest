

from NovaPoshta.Core.ApiModel import ApiModel

class ContactPerson(ApiModel):
    """
    ContactPerson - Модель для создания контактного лица  Class ContactPerson
    """
        
    def save(self):
        """
        Вызвать метод save() - сохранить данные контактного лица отправителя/получателя

        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return self._sendData('save', self)

    def update(self):
        """
        Вызвать метод update() - обновить данные контактного лица

        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return self._sendData('update', self)

    def delete(self):
        """
        Вызвать метод delete() - удалить контактное лицо отправителя/получателя

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
        
        return self.Emailf