

from NovaPoshta.MethodParameters.MethodParameters import MethodParameters

class Counterparty_getCounterpartyContactPersons(MethodParameters):
    """
    Параметры метода getCounterpartyContactPersons модели Counterparty
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
        Получить реф

        :return: str
        """
        
        return self.Ref

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