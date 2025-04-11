import uuid
from datetime import datetime

from src.models.base import Entity
from src.value_objects.title import Title


class User(Entity):
    __id: uuid.UUID
    __name: str
    __registered_at: datetime.date

    def __init__(
        self, name: str, publishing_date: datetime.date, publisher: str
    ) -> None:
        super().__init__()
        self.__id = uuid.uuid4()
        self.__name = name
        self.__registered_at = publishing_date

    @property
    def id(self) -> uuid.UUID:
        return self.__id
