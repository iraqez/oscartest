

from NovaPoshta.MethodParameters.MethodParameters import MethodParameters

class Common_getTimeIntervals(MethodParameters):
    """
    Параметры метода getTimeIntervals модели Common
    """
        
    def setRecipientCityRef(self, value):
        """
        Устанавливает получателя реф города

        :type value: str
        :return: self
        """
        
        self.RecipientCityRef = value
        return self

    def getRecipientCityRef(self):
        """
        Получает получателя реф города

        :return: str
        """
        
        return self.RecipientCityRef

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
        Получает дату

        :return: str
        """
        
        return self.DateTime