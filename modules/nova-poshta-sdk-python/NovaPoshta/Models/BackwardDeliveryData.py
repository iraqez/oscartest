

from NovaPoshta.Core.BaseModel import BaseModel

class BackwardDeliveryData(BaseModel):
    """
    Параметры обратной доставки
    """
        
    def setPayerType(self, value):
        """
        Устанавливает тип плательщика

        :type value: str
        :return: self
        """
        
        self.PayerType = value
        return self

    def getPayerType(self):
        """
        Возвращает тип плательщика

        :return: str
        """
        
        return self.PayerType

    def setCargoType(self, value):
        """
        Устанавливает тип груза

        :type value: str
        :return: self
        """
        
        self.CargoType = value
        return self

    def getCargoType(self):
        """
        Возвращает тип груза

        :return: str
        """
        
        return self.CargoType

    def setRedeliveryString(self, value):
        """
        Устанавливает описания груза

        :type value: str
        :return: self
        """
        
        self.RedeliveryString = value
        return self

    def getRedeliveryString(self):
        """
        Возвращает описания груза

        :return: str
        """
        
        return self.RedeliveryString

    def addTray(self, cargo):
        """
        Добавляет поддон

        :type cargo: NovaPoshta.Models.Cargo.Cargo
        :return: self
        """
        
        if self.Trays is None:
            self.Trays = []
        self.Trays.append(cargo)
        return self

    def setTrays(self, trays):
        """
        Устанавливает поддон

        :type value: list
        :return: self
        """
        
        self.Trays = trays
        return self

    def getTrays(self):
        """
        Возвращает поддоны

        :return: list
        """
        
        return self.Trays

    def clearTrays(self):
        """
        Очищает поддоны

        :return: self
        """
        
        self.Trays = []
        return self