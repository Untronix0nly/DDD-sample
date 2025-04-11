import datetime

from src.events.loan.LoanCreated import LoanCreated
from src.models.base import Entity
from src.models.book import Book
from src.models.user import User


class Loan(Entity):
    def __init__(self, book: Book, user: User):
        super().__init__()
        self.book = book
        self.user = user
        self.add_event(
            LoanCreated(
                esbn=book.esbn.esbn,
                user_id=user.id,
                date=datetime.datetime.now(datetime.timezone.utc),
            )
        )

    def return_book(self):
        self.book.return_book()
