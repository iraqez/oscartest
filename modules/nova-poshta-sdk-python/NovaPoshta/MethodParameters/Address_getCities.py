

from NovaPoshta.MethodParameters.MethodParameters import MethodParameters

class Address_getCities(MethodParameters):
    """
    Параметры метода getCities модели Address  Class
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

        return self.Ref

    def setFindBystr(self, value):
        """
        Устанавливает строку для поиска города

        :type value: str
        :return: self
        """

        self.FindBystr = value
        return self

    def getFindBystr(self):
        """
        Возвращает строку для поиска города

        :return: str
        """

        return self.FindBystr

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