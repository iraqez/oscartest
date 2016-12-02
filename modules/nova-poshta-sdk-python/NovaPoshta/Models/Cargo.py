

from NovaPoshta.Core.BaseModel import BaseModel

class Cargo(BaseModel):
    """
    Груз
    """
    def setCargoDescription(self, value):
        """
        Устанавливает реф груза

        :type value: str
        :return: self
        """
        self.CargoDescription = value
        return self

    def getCargoDescription(self):
        """
        Возвращает реф груза

        :return: str
        """
        return self.Amount

    def setAmount(self, value):
        """
        Устанавливает количество груза

        :type value: int
        :return: self
        """
        self.Amount = value
        return self

    def getAmount(self):
        """
        Возвращает количество груза

        :return: int
        """
        return self.Amount