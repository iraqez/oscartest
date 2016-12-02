

from NovaPoshta.MethodParameters.MethodParameters import MethodParameters

class InternetDocument_getDocumentList(MethodParameters):
    """
    Параметры метода getDocumentList модели InternetDocument
    """
        
    # Сортировка по убыванию
    ORDER_DIRECTION_DESC = 'DESC'
    # Сортировка по возрастанию
    ORDER_DIRECTION_ASC = 'ASC'
    # Сортировка по полю номер документа
    ORDER_FIELD_IntDocNumber = 'IntDocNumber'
    # Сортировка по полю дата отправки
    ORDER_FIELD_DateTime = 'DateTime'
    # Сортировка по полю вес
    ORDER_FIELD_Weight = 'Weight'
    # Сортировка по полю стоимость товара
    ORDER_FIELD_Cost = 'Cost'
    # Сортировка по полю количество мест
    ORDER_FIELD_SeatsAmount = 'SeatsAmount'
    # Сортировка по полю цена доставки
    ORDER_FIELD_CostOnSite = 'CostOnSite'
    # Сортировка по полю дата создания
    ORDER_FIELD_CreateTime = 'CreateTime'
    # Сортировка по полю дата доставки
    ORDER_FIELD_EstimatedDeliveryDate = 'EstimatedDeliveryDate'
    # Сортировка по полю статус доставки
    ORDER_FIELD_StateId = 'StateId'
    # Сортировка по полю внутренний номер
    # клиента
    ORDER_FIELD_InfoRegClientBarcodes = 'InfoRegClientBarcodes'
    # Сортировка по полю дата фактическая дата
    # доставки
    ORDER_FIELD_RecipientDateTime = 'RecipientDateTime'

    def setIntDocNumber(self, value):
        """
        Устанавливает номер документа

        :type value: str
        :return: self
        """
        
        self.IntDocNumber = value
        return self

    def getIntDocNumber(self):
        """
        Получить номер документа

        :return: str
        """
        
        return self.IntDocNumber

    def setInfoRegClientBarcodes(self, value):
        """
        Устанавливает номер внутреннего заказа
        клиента

        :type value: str
        :return: self
        """
        
        self.InfoRegClientBarcodes = value
        return self

    def getInfoRegClientBarcodes(self):
        """
        Получить номер внутреннего заказа клиента

        :return: str
        """
        
        return self.InfoRegClientBarcodes

    def setDeliveryDateTime(self, value):
        """
        Устанавливает дата доставки

        :type value: str
        :return: self
        """
        
        self.DeliveryDateTime = value
        return self

    def getDeliveryDateTime(self):
        """
        Получить дата доставки

        :return: str
        """
        
        return self.DeliveryDateTime

    def setRecipientDateTime(self, value):
        """
        Устанавливает фактическую дату и время
        получения

        :type value: str
        :return: self
        """
        
        self.RecipientDateTime = value
        return self

    def getRecipientDateTime(self):
        """
        Получить фактическую дату и время
        получения

        :return: str
        """
        
        return self.RecipientDateTime

    def setCreateTime(self, value):
        """
        Устанавливает дату и время создания ЕН

        :type value: str
        :return: self
        """
        
        self.CreateTime = value
        return self

    def getCreateTime(self):
        """
        Получить дату и время создания ЕН

        :return: str
        """
        
        return self.CreateTime

    def setSenderRef(self, value):
        """
        Устанавливает идентификатор отправителя

        :type value: str
        :return: self
        """
        
        self.SenderRef = value
        return self.SenderRef

    def getSenderRef(self):
        """
        Получить идентификатор отправителя

        :return: str
        """
        
        return self.SenderRef

    def setRecipientRef(self, value):
        """
        Устанавливает идентификатор получателя

        :type value: str
        :return: self
        """
        
        self.RecipientRef = value
        return self

    def getRecipientRef(self):
        """
        Получить идентификатор получателя

        :return: str
        """
        
        return self.RecipientRef

    def setWeightFrom(self, value):
        """
        Устанавливает вес от

        :type value: float
        :return: self
        """
        
        self.WeightFrom = value
        return self

    def getWeightFrom(self):
        """
        Получить вес от

        :return: float
        """
        
        return self.WeightFrom

    def setWeightTo(self, value):
        """
        Устанавливает вес до

        :type value: float
        :return: self
        """
        
        self.WeightTo = value
        return self

    def getWeightTo(self):
        """
        Получить вес до

        :return: float
        """
        
        return self.WeightTo

    def setCostFrom(self, value):
        """
        Устанавливает объявленную стоимость от

        :type value: float
        :return: self
        """
        
        self.CostFrom = value
        return self

    def getCostFrom(self):
        """
        Получить объявленную стоимость от

        :return: float
        """
        
        return self.CostFrom

    def setCostTo(self, value):
        """
        Устанавливает объявленную стоимость до

        :type value: float
        :return: self
        """
        
        self.CostTo = value
        return self

    def getCostTo(self):
        """
        Получить объявленную стоимость до

        :return: float
        """
        
        return self.CostTo

    def setSeatsAmountFrom(self, value):
        """
        Устанавливает количество мест от

        :type value: float
        :return: self
        """
        
        self.SeatsAmountFrom = value
        return self

    def getSeatsAmountFrom(self):
        """
        Получить количество мест от

        :return: float
        """
        
        return self.SeatsAmountFrom

    def setSeatsAmountTo(self, value):
        """
        Устанавливает количество мест до

        :type value: float
        :return: self
        """
        
        self.SeatsAmountTo = value
        return self

    def getSeatsAmountTo(self):
        """
        Получить количество мест до

        :return: float
        """
        
        return self.SeatsAmountTo

    def setCostOnSiteFrom(self, value):
        """
        Устанавливает стоимость доставки от

        :type value: float
        :return: self
        """
        
        self.CostOnSiteFrom = value
        return self

    def getCostOnSiteFrom(self):
        """
        Получить стоимость доставки от

        :return: float
        """
        
        return self.CostOnSiteFrom

    def setCostOnSiteTo(self, value):
        """
        Устанавливает стоимость доставки до

        :type value: float
        :return: self
        """
        
        self.CostOnSiteTo = value
        return self

    def getCostOnSiteTo(self):
        """
        Получить стоимость доставки до

        :return: float
        """
        
        return self.CostOnSiteTo

    def setStateIds(self, value):
        """
        Устанавливает статусы

        :type value: list
        :return: self
        """
        
        self.StateIds = value
        return self

    def getStateIds(self):
        """
        Получить статусы

        :return: list
        """
        
        return self.StateIds

    def setDateTime(self, value):
        """
        Устанавливает дату отправки

        :type value: str
        :return: self
        """
        
        self.DateTime = value
        return self

    def getDateTime(self):
        """
        Получить дату отправки

        :return: str
        """
        
        return self.DateTime

    def setDateTimeFrom(self, value):
        """
        Устанавливает дату отправки от

        :type value: str
        :return: self
        """
        
        self.DateTimeFrom = value
        return self

    def getDateTimeFrom(self):
        """
        Получить дату отправки от

        :return: str
        """
        
        return self.DateTimeFrom

    def setDateTimeTo(self, value):
        """
        Устанавливает дату отправки до

        :type value: str
        :return: self
        """
        
        self.DateTimeTo = value
        return self

    def getDateTimeTo(self):
        """
        Получить дату отправки до

        :return: str
        """
        
        return self.DateTimeTo

    def setIsAfterpayment(self, value):
        """
        Устанавливает контроль оплаты

        :type value: bool
        :return: self
        """
        
        self.isAfterpayment = value
        return self

    def getIsAfterpayment(self):
        """
        Получить контроль оплаты

        :return: bool
        """
        
        return self.isAfterpayment

    def setPage(self, value):
        """
        Устанавливает страницу

        :type value: int
        :return: self
        """
        
        self.Page = value
        return self

    def getPage(self):
        """
        Получитьстраницу

        :return: int
        """
        
        return self.Page

    def setOrderField(self, value):
        """
        Устанавливает параметр сортировки

        :type value: str
        :return: self
        """
        
        self.OrderField = value
        return self

    def getOrderField(self):
        """
        Получить параметр сортировки

        :return: str
        """
        
        return self.OrderField

    def setOrderDirection(self, value):
        """
        Устанавливает порядок сортировки

        :type value: str
        :return: self
        """
        
        self.OrderDirection = value
        return self

    def getOrderDirection(self):
        """
        Получить порядок сортировки

        :return: str
        """
        
        return self.OrderDirection

    def setScanSheetRef(self, value):
        """
        Устанавливает реф реестра

        :type value: str
        :return: self
        """
        
        self.ScanSheetRef = value
        return self

    def getScanSheetRef(self):
        """
        Получить реф реестра

        :return: str
        """
        
        return self.ScanSheetRef