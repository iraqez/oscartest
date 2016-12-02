

from NovaPoshta.MethodParameters.MethodParameters import MethodParameters

class InternetDocument_getDocumentPrice(MethodParameters):
    """
    Параметры метода getDocumentPrice модели InternetDocument Class InternetDocument_documentsTracking
    """
        
    def setCitySender(self, value):
        """
        Устанавливает реф города отправителя
        """
        
        self.CitySender = value
        return self

    def getCitySender(self):
        """
        Получить реф города отправителя

        :return: str
        """
        
        return self.CitySender

    def setCityRecipient(self, value):
        """
        Устанавливает реф города получателя
           
        :type value: str   
        :return: self
        """
        
        self.CityRecipient = value
        return self

    def getCityRecipient(self):
        """
        Получить реф города получателя

        :return: str
        """
        
        return self.CityRecipient

    def setServiceType(self, value):
        """
        Устанавливает технологию доставки
           
        :type value: str   
        :return: self
        """
        
        self.ServiceType = value
        return self

    def getServiceType(self):
        """
        Получить технологию доставки

        :return: str
        """
        
        return self.ServiceType

    def setWeight(self, value):
        """
        Устанавливает вес
           
        :type value: float
        :return: self
        """
        
        self.Weight = value
        return self

    def getWeight(self):
        """
        Получить вес

        :return: float
        """
        
        return self.Weight

    def setCost(self, value):
        """
        Устанавливает цену
           
        :type value: float
        :return: self
        """
        
        self.Cost = value
        return self

    def getCost(self):
        """
        Получить цену

        :return: float
        """
        
        return self.Cost

    def setDateTime(self, value):
        """
        Устанавливает дату
           
        :type value: str   
        :return: self
        """
        
        self.DateTime = value
        return self

    def getDateTime(self):
        """
        Получить дату

        :return: str
        """
        
        return self.DateTime