

from NovaPoshta.MethodParameters.MethodParameters import MethodParameters

class ScanSheet_removeDocuments(MethodParameters):
    """
    Параметры метода removeDocuments модели ScanSheet
    """

    def setDocumentRefs(self, documentRefs):
        """
        Устанавливает рефы реестров

        :type value: list
        :return: self
        """
        
        self.DocumentRefs = documentRefs
        return self

    def getDocumentRefs(self):
        """
        Получить рефы реестров

        :return: list
        """
        if self.DocumentRefs is None:
            self.DocumentRefs = []
        
        return self.DocumentRefs

    def addDocumentRef(self, value):
        """
        Добавить реф реестра

        :type value: str
        :return: self
        """

        if self.DocumentRefs is None:
            self.DocumentRefs = []
        self.DocumentRefs.append(value)
        return self

    def clearDocumentRefs(self):
        """
        Очистить рефы реестров

        :type value: str
        :return: self
        """
        
        self.DocumentRefs = []
        return self