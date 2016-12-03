

from NovaPoshta.MethodParameters.MethodParameters import MethodParameters

class Address_getStreet(MethodParameters):
    """
    Параметры метода getStreet модели Address  Class
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
        """Возвращает реф города
           @param $value
           @return str
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

    def setFindBystr(self, value):
        """
        Устанавливает строку для поиска улицы

        :type value: str
        :return: self
        """

        self.FindBystr = value
        return self

    def getFindBystr(self):
        """
        Возвращает строку для поиска улицы

        :return: str
        """

        return self.FindBystr