

from NovaPoshta.MethodParameters.MethodParameters import MethodParameters

class Counterparty_getCounterpartyByEDRPOU(MethodParameters):
    """
    Параметры метода getCounterpartyByEDRPOU модели
    """
        
    def setEDRPOU(self, value):
        """
        Устанавливает ОКПО

        :type value: str
        :return: self
        """
        
        self.EDRPOU = value
        return self

    def getEDRPOU(self):
        """
        Получить ОКПО

        :return: str
        """
        
        return self.EDRPOU

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