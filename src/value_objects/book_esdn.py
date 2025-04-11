import uuid


class BookESDN:
    __esdn: uuid.UUID

    def __init__(self, esdn: uuid.UUID):
        self.__esdn = esdn

    def __eq__(self, other):
        return self.__esdn == other.__esdn

    @property
    def esbn(self) -> uuid.UUID:
        return self.__esdn

    def __hash__(self):
        return hash(self.__esdn)
