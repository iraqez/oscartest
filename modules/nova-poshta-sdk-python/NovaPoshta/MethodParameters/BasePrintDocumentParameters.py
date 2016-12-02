

from NovaPoshta.MethodParameters.MethodParameters import MethodParameters

class BasePrintDocumentParameters(MethodParameters):
    """
    Class BasePrintDocumentParameters
    """
        
    def setDocumentRefs(self, documentRefs):
        """
        Устанавливает рефы документов

        :type documentRefs: list
        :return: self
        """
        
        self.DocumentRefs = documentRefs
        return self

    def getDocumentRefs(self):
        """
        Возвращает рефы документов

        :return: list
        """
        
        return self.DocumentRefs

    def clearDocumentRefs(self):
        """
        Очищает рефы документов

        :return: list
        """
        
        self.DocumentRefs = []
        return self

    def addDocumentRef(self, value):
        """
        Добавляет реф документа

        :type value: str
        :return: self
        """
        
        if self.DocumentRefs is None:
            self.DocumentRefs = []
        self.DocumentRefs.append(value)
        return self

    def setType(self, value):
        """
        Устанавливает тип печати

        :type value: str
        :return: self
        """
        
        self.Type = value
        return self

    def getType(self):
        """
        Возвращает тип печати

        :return: str
        """
        
        return self.Type

    def setCopies(self, value):
        """
        Устанавливает количество копий

        :type value: int
        :return: self
        """
        
        self.Copies = value
        return self

    def getCopies(self):
        """
        Возвращает количество копий

        :return: int
        """
        
        return self.Copies