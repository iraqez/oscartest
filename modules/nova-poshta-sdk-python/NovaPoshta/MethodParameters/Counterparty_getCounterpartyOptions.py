

from NovaPoshta.MethodParameters.MethodParameters import MethodParameters

class Counterparty_getCounterpartyOptions(MethodParameters):
    """
        Параметры метода getCounterpartyOptions модели Counterparty
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