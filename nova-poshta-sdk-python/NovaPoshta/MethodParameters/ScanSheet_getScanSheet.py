

from NovaPoshta.MethodParameters.MethodParameters import MethodParameters

class ScanSheet_getScanSheet(MethodParameters):
    """
    Параметры метода getScanSheet модели ScanSheet
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