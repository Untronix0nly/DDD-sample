import uuid

from sqlalchemy import UUID, Boolean, Column, DateTime, String, Table, Text
from sqlalchemy.orm import column_property, registry

from src.models.book import Book

mapper_registry = registry()


book_table = Table(
    "books",
    mapper_registry.metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column("name", Text),
    Column("publishing_date", DateTime(timezone=True)),
    Column("publisher", Text),
    Column("is_loan", Boolean),
)


def start_mapping():
    mapper_registry.map_imperatively(
        Book,
        book_table,
        properties={
            "__esbn": column_property(book_table.c.id),
            "__name": column_property(book_table.c.name),
            "__publishing_date": column_property(book_table.c.publishing_date),
            "__publisher": column_property(book_table.c.publisher),
            "__is_loan": column_property(book_table.c.is_loan),
        },
    )
