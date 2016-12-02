

from NovaPoshta.MethodParameters.MethodParameters import MethodParameters

class InternetDocument_getDocument(MethodParameters):
    """
    Параметры метода getDocument модели InternetDocument
    """
        
    def setRef(self, value):
        """
        Устанавливает реф документа

        :type value: str
        :return: self
        """
        
        self.Ref = value
        return self

    def getRef(self):
        """
        Получить реф документа

        :return: str
        """
        
        return self.Ref