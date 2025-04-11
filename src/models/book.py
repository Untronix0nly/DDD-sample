import datetime
import uuid

from src.domain_exceptions.book_is_loaned_exception import BookIsLoanedException
from src.events.book.book_returned import BookReturned
from src.models.base import Entity
from src.value_objects.book_esdn import BookESDN
from src.value_objects.title import Title


class Book(Entity):
    __esbn: BookESDN
    __name: Title
    __publishing_date: datetime.date
    __publisher: str
    __is_loan: bool  # enum

    def __init__(
        self, name: Title, publishing_date: datetime.date, publisher: str
    ) -> None:
        super().__init__()
        self.__esbn = BookESDN(uuid.uuid4())
        self.__name = name
        self.__publishing_date = publishing_date
        self.__publisher = publisher
        self.__is_loan = False

    def loan(self):
        if not self.__is_loan:
            self.__is_loan = True
        else:
            raise BookIsLoanedException("Book is already loaned")

    def return_book(self):
        if self.__is_loan:
            self.__is_loan = False
            self.add_event(
                BookReturned(
                    esbn=self.__esbn.esbn,
                    date=datetime.datetime.now(datetime.timezone.utc),
                )
            )

    @property
    def esbn(self) -> BookESDN:
        return self.__esbn
