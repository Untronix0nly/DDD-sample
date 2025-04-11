import abc


class DomainEvent(abc.ABC): ...


class Entity(abc.ABC):
    events: list[DomainEvent]

    def __init__(self):
        self.events = []

    def add_event(self, event: DomainEvent):
        self.events.append(event)

    def clear(self):
        self.events = []

    def get_events(self):
        return self.events[:]
