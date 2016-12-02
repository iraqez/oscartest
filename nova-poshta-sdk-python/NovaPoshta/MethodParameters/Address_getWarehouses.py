

from NovaPoshta.MethodParameters.MethodParameters import MethodParameters

class Address_getWarehouses(MethodParameters):
    """
    Параметры метода getWarehouses модели Address  Class
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
        Возвращает реф города

        :return: str
        """
        
        return self.CityRef

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
        Возвращает страницу

        :return: int
        """
        
        return self.Page