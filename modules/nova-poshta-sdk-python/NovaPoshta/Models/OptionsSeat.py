

from NovaPoshta.Core.BaseModel import BaseModel

class OptionsSeat(BaseModel):
    """
    Параметры груза  Class OptionsSeat
    """

    def setVolumetricVolume(self, value):
        """
        Устанавливает объем

        :type value: str
        :return: self
        """

        self.volumetricVolume = value
        return self

    def getVolumetricVolume(self):
        """
        Возвращает объем

        :return: str
        """

        return self.volumetricVolume

    def setVolumetricWidth(self, value):
        """
        Устанавливает ширину

        :type value: str
        :return: self
        """

        self.volumetricWidth = value
        return self

    def getVolumetricWidth(self):
        """
        Возвращает ширину

        :return: str
        """

        return self.volumetricWidth

    def setVolumetricLength(self, value):
        """
        Устанавливает длину

        :type value: str
        :return: self
        """

        self.volumetricLength = value
        return self

    def getVolumetricLength(self):
        """
        Возвращает длину

        :return: str
        """

        return self.volumetricLength

    def setVolumetricHeight(self, value):
        """
        Устанавливает высоту

        :type value: str
        :return: self
        """

        self.volumetricHeight = value
        return self

    def getVolumetricHeight(self):
        """
        Возвращает высоту

        :return: str
        """

        return self.volumetricHeight

    def setWeight(self, value):
        """
        Устанавливает вес

        :type value: str
        :return: self
        """

        self.weight = value
        return self

    def getWeight(self):
        """
        Возвращает вес

        :return: str
        """

        return self.weight