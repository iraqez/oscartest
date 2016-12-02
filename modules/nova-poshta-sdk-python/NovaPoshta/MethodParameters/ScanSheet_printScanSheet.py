

from NovaPoshta.MethodParameters.BasePrintDocumentParameters import BasePrintDocumentParameters

class ScanSheet_printScanSheet(BasePrintDocumentParameters):
    """
    Параметры метода printScanSheet модели ScanSheet
    """
        
    def addNumber(self, value):
        """
        Добавляет номер реестра

        :type value: str
        :return: self
        """
        
        self.addDocumentRef(value)
        return self

    def setNumbers(self, numbers):
        """
        Устанавливает номера реестров

        :type value: str
        :return: self
        """
        
        self.setDocumentRefs(numbers)
        return self

    def getNumbers(self):
        """
        Возвращает номера реестров
           @return str
        """
        
        return self.getDocumentRefs()

    def clearNumbers(self):
        """
        Очищает номера реестров

        :return: str
        """
        
        self.clearDocumentRefs()