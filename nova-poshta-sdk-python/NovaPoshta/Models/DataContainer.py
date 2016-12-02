

from NovaPoshta.Core.BaseModel import BaseModel

class DataContainer(BaseModel):
    """
    Объект для формирования запроса  Class DataContainer
    """

    apiKey = None
    modelName = None
    id = None
    calledMethod = None
    methodProperties = None
    language = None