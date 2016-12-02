

from NovaPoshta.Core.BaseModel import BaseModel

class CounterpartyContact(BaseModel):
    """
    Контрагент
    """
    def setRef(self, value):
        """
        Устанавливает реф

        :type value: str
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

    def setCity(self, value):
        """
        Устанавливает реф города

        :type value: str
        :return: self
        """

        self.City = value
        return self

    def getCity(self):
        """
        Возвращает реф города

        :return: str
        """

        return self.City

    def setAddress(self, value):
        """
        Устанавливает

        :type value: str
        :return: self
        """

        self.Address = value
        return self

    def getAddress(self):
        """
        Возвращает адрес

        :return: str
        """

        return self.Address

    def setContact(self, value):
        """
        Устанавливает контактное лицо

        :type value: str
        :return: self
        """

        self.Contact = value
        return self

    def getContact(self):
        """
        Возвращает контактное лицо

        :return: str
        """

        return self.Contact

    def setPhone(self, value):
        """
        Устанавливает номер телефона

        :type value: str
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