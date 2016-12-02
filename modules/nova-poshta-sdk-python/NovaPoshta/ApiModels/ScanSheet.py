

from NovaPoshta.Core.ApiModel import ApiModel

class ScanSheet(ApiModel):
    """
    ScanSheet - Модель для работы с реестрами приема-передачи отправлений
    """

    # Печать в формате PDF
    PRINT_TYPE_PDF = 'pdf'
    # Печать в формате HTML
    PRINT_TYPE_HTML = 'html'

    def save(self):
        """
        Сохранить экспресс-накладные в реестр Реализация метода insertDocuments() - добавить
        экспресс-накладные в реестр

        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        self.Ref = None
        return ScanSheet._sendData(ScanSheet, 'insertDocuments', self)

    def update(self):
        """
        Обновить экспресс-накладные в реестр
        Реализация метода insertDocuments() - добавить экспресс-накладные в реестр

        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return ScanSheet._sendData(ScanSheet, 'insertDocuments', self)

    def delete(self):
        """
        Удалить реестр  Реализация метода deleteScanSheet() - удалить (расформировать) реестр отправлений

        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        self.DocumentRefs = [self.Ref]
        return ScanSheet._sendData(ScanSheet, 'deleteScanSheet', self)

    def setDocumentRefs(self, documentRefs):
        """
        Устанавливает документы

        :param documentRefs: list
        :return: self
        """
        
        self.DocumentRefs = documentRefs
        return self

    def addDocumentRef(self, value):
        """
        Добавить реф документа

        :param value: str
        :return: self
        """
        
        if self.DocumentRefs is None:
            self.DocumentRefs = []
        self.DocumentRefs.append(value)
        return self

    def clearDocumentRefs(self):
        """
        Очистить рефы документов

        :return: self
        """
        
        self.DocumentRefs = []
        return self

    def setRef(self, value):
        """
        Устанавливает реф реестра

        :param value: str
        :return: self
        """
        
        self.Ref = value
        return self

    def getRef(self):
        """
        Возвращает реф реестра

        :return: str
        """
        
        return self.Ref

    def setDate(self, value):
        """
        Устанавливает дату

        :param value: str
        :return: self
        """
        
        self.Date = value
        return self

    def getDate(self):
        """
        Возвращает дату

        :return: str
        """
        
        return self.Date

    @staticmethod
    def removeDocuments(data = None):
        """
        Вызвать метод removeDocuments() - удалить экспресс-накладные из реестра

        :type data: NovaPoshta.MethodParameters.MethodParameters.MethodParameters
        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        # todo падає скрипт
        return ScanSheet._sendData(ScanSheet, 'removeDocuments', data)

    @staticmethod
    def getScanSheet(data = None):
        """
        Вызвать метод getScanSheet() - загрузить информацию по одному реестру

        :type data: NovaPoshta.MethodParameters.MethodParameters.MethodParameters
        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return ScanSheet._sendData(ScanSheet, 'getScanSheet', data)

    @staticmethod
    def getScanSheetList(data = None):
        """
        Вызвать метод getScanSheetList() - загрузить список реестров

        :type data: NovaPoshta.MethodParameters.MethodParameters.MethodParameters
        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return ScanSheet._sendData(ScanSheet, 'getScanSheetList', data)

    @staticmethod
    def printScanSheet(data = None):
        """
        Вызвать метод printScanSheet() - загрузка печатной
        формы реестра

        :type data: NovaPoshta.MethodParameters.MethodParameters.MethodParameters
        :return: str
        """
        
        # todo there is print for scanSheet
        return ScanSheet._sendData(ScanSheet, 'printScanSheet', data)