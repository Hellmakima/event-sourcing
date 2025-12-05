from enum import StrEnum
from dataclasses import dataclass, field
from datetime import datetime

class EventType(StrEnum):
    ITEM_ADDED = "ITEM_ADDED"
    ITEM_REMOVED = "ITEM_REMOVED"

@dataclass(frozen=True)
class Event[T = str]:
    """Represents an event in the event store."""
    event_type: EventType
    data: T
    timestamp: datetime = field(default_factory=datetime.now)
