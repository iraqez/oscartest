

from NovaPoshta.MethodParameters.MethodParameters import MethodParameters

class Counterparty_getCounterparties(MethodParameters):
    """
    Параметры метода getCounterparties модели Counterparty
    """
        
    def setRef(self, value):
        """
        Идентификатор контрагента

        :type value: str
        :return: self
        """
        
        self.Ref = value
        return self

    def getRef(self):
        """
        Возвращает реф

        :return:
        """
        
        return self.Ref

    def setCounterpartyProperty(self, value):
        """
        Устанавливает свойство контрагента

        :type value: str
        :return: self
        """
        
        self.CounterpartyProperty = value
        return self

    def getCounterpartyProperty(self):
        """
        Получить свойство контрагента

        :return: str
        """
        
        return self.CounterpartyProperty

    def setPage(self, value):
        """
        Устанавливает страницу

        :type value: int
        :return: self
        """
        
        self.Page = value
        return self

    def getPage(self):
        """
        Получить страницу

        :return: int
        """
        
        return self.Page

    def setFindByString(self, value):
        """
        Устанавливает строку для поиска
        контрагента

        :type value: str
        :return: self
        """
        
        self.FindByString = value
        return self

    def getFindByString(self):
        """
        Получить строку для поиска контрагента

        :return: str
        """
        
        return self.FindByString

    def setCityRef(self, value):
        """
        Устанавливает реф города

        :type value: str
        :return: self
        """
        
        self.CityRef = value
        return self

    def getCityRef(self):
        """
        Получить реф города

        :return: str
        """
        
        return self.CityRef