

from NovaPoshta.MethodParameters.MethodParameters import MethodParameters

class InternetDocument_documentsTracking(MethodParameters):
    """
    Параметры метода documentsTracking модели InternetDocument
    """
        
    def setDocuments(self, value):
        """
        Устанавливает номера документов

        :type value: list
        :return: self
        """
        
        self.Documents = value
        return self

    def getDocuments(self):
        """
        Устанавливает номер документа

        :return: list
        """

        if self.Documents is None:
            self.Documents = []
        return self.Documents

    def addDocument(self, value):
        """
        Добавить номер документа

        :type value: str
        :return: self
        """
        
        if self.Documents is None:
            self.Documents = []
        self.Documents.append(value)
        return self

    def clearDocuments(self):
        """
        Очищить номера документов

        :return: self
        """
        
        self.Documents = []
        return self