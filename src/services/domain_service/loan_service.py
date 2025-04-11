from src.models.book import Book
from src.models.loan import Loan
from src.models.user import User


class LoanService:
    def loan_book(self, book: Book, user: User) -> Loan:
        book.loan()
        return Loan(book, user)

    def return_book(self, loan: Loan):
        loan.return_book()
