import datetime
import uuid
from dataclasses import dataclass

from src.models.base import DomainEvent


@dataclass
class BookReturned(DomainEvent):
    esbn: uuid.UUID
    date: datetime.datetime
