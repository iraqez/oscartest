

from NovaPoshta.Core.ApiModel import ApiModel

class Common(ApiModel):
    """
    Common - Модель для работы со справочниками
    """
        
    @staticmethod
    def getBackwardDeliveryCargoTypes():
        """
        Вызвать метод getBackwardDeliveryCargoTypes() - получить список видов обратной доставки груза

        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return ApiModel._sendData(Common, 'getBackwardDeliveryCargoTypes')

    @staticmethod
    def getCargoDescriptionList(data=None):
        """
        Вызвать метод getCargoDescriptionList() - загрузить справочник описания груза

        :type data: NovaPoshta.MethodParameters.MethodParameters.MethodParameters
        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return ApiModel._sendData(Common, 'getCargoDescriptionList', data)

    @staticmethod
    def getCargoTypes():
        """
        Вызвать метод getCargoTypes() - загрузить список видов груза

        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return ApiModel._sendData(Common, 'getCargoTypes')

    @staticmethod
    def getDocumentStatuses():
        """
        Вызвать метод getDocumentStatuses() - загрузить список статусов документов

        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return ApiModel._sendData(Common, 'getDocumentStatuses')

    @staticmethod
    def getOwnershipFormsList():
        """
        Вызвать метод getOwnershipFormsList() - загрузить список форм собственности

        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return ApiModel._sendData(Common, 'getOwnershipFormsList')

    @staticmethod
    def getPalletsList():
        """
        Вызвать метод getPalletsList() - загрузить список поддонов (при заказе услуги обратная доставка  поддонов)

        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return ApiModel._sendData(Common, 'getPalletsList')

    @staticmethod
    def getPaymentForms():
        """
        Вызвать метод getPaymentForms() - загрузить список форм оплаты

        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return ApiModel._sendData(Common, 'getPaymentForms')

    @staticmethod
    def getServiceTypes():
        """
        Вызвать метод getServiceTypes() - загрузить справочник технологий доставки

        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return ApiModel._sendData(Common, 'getServiceTypes')

    @staticmethod
    def getTimeIntervals(data=None):
        """
        Вызвать метод getTimeIntervals() - загрузить список временных интервалов (для заказа услуги "Временные интервалы")

        :type data: NovaPoshta.MethodParameters.MethodParameters.MethodParameters
        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return ApiModel._sendData(Common, 'getTimeIntervals', data)

    @staticmethod
    def getTiresWheelsList():
        """
        Вызвать метод getTiresWheelsList() - загрузить список шин и дисков (если вид груза "шины- диски")

        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return ApiModel._sendData(Common, 'getTiresWheelsList')

    @staticmethod
    def getTraysList():
        """
        Вызвать метод getTraysList() - загрузить список поддонов (если заказана услуга обратной доставки поддонов)

        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return ApiModel._sendData(Common, 'getTraysList')

    @staticmethod
    def getTypesOfCounterparties():
        """
        Вызвать метод getTypesOfCounterparties() - загрузить список типов контрагентов отправителей

        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return ApiModel._sendData(Common, 'getTypesOfCounterparties')

    @staticmethod
    def getTypesOfPayers():
        """
        Вызвать метод getTypesOfPayers() - загрузить список видов плательщиков

        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return ApiModel._sendData(Common, 'getTypesOfPayers')

    @staticmethod
    def getTypesOfPayersForRedelivery():
        """
        Вызвать метод getTypesOfPayersForRedelivery() - загрузить список видов плательщиков обратной доставки

        :return: NovaPoshta.Models.DataContainerResponse.DataContainerResponse
        """
        
        return ApiModel._sendData(Common, 'getTypesOfPayersForRedelivery')
