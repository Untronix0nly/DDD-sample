import datetime
import uuid
from dataclasses import dataclass

from src.models.base import DomainEvent


@dataclass
class LoanCreated(DomainEvent):
    esbn: uuid.UUID
    date: datetime.date
    user_id: uuid.UUID
