

from NovaPoshta.MethodParameters.MethodParameters import MethodParameters

class InternetDocument_getDocumentDeliveryDate(MethodParameters):
    """
    Параметры метода getDocumentDeliveryDate модели InternetDocument
    """
        
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

    def setCitySender(self, value):
        """
        Устанавливает реф города отправителя

        :type value: str
        :return: self
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