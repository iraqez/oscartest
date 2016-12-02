

from NovaPoshta.MethodParameters.MethodParameters import MethodParameters

class Address_getAreas(MethodParameters):
    """
    Параметры метода getAreas модели Address  Class
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

        return self.Page

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