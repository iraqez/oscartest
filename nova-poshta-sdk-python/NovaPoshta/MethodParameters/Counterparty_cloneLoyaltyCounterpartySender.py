

from NovaPoshta.MethodParameters.MethodParameters import MethodParameters

class Counterparty_cloneLoyaltyCounterpartySender(MethodParameters):
    """
    Параметры метода cloneLoyaltyCounterpartySender модели Counterparty
    """
        
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