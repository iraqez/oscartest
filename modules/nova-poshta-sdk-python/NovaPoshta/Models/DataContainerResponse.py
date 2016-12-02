

from NovaPoshta.Core.BaseModel import BaseModel

class DataContainerResponse(BaseModel):
    """
    Контейнер с ответом сервера
    """

    id = None
    success = None
    data = []
    errors = []
    warnings = []
    info = []