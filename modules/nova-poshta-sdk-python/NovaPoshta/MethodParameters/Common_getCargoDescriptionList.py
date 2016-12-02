

from NovaPoshta.MethodParameters.MethodParameters import MethodParameters

class Common_getCargoDescriptionList(MethodParameters):
    """
    Параметры метода getCargoDescriptionList модели Common
    """
        
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
        Получает страницу

        :return: int
        """
        
        return self.Page

    def setFindByString(self, value):
        """
        Устанавливает строку для поиска описания
        груза

        :type value: str
        :return: self
        """
        
        self.FindByString = value
        return self

    def getFindByString(self):
        """
        Получает строку для поиска описания груза

        :return: str
        """
        
        return self.FindByString