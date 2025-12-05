from collections import Counter, defaultdict
from event import EventType
from event_store import EventStore
from item import Item

def get_most_collected_items(event_store: EventStore[Item], limit: int = 2) -> list[tuple[str, int]]:
    """ Returns a list of most frequently added items. """
    counts = Counter[str]()
    for event in event_store.get_events():
        item_name = event.data.name
        if event.event_type == EventType.ITEM_ADDED:
            counts[item_name] += 1

    return counts.most_common(limit)

def get_item_origins(event_store: EventStore[Item]) -> dict[str, set[str]]:
    """ Returns mapping of items and their origins. """
    origins: dict[str, set[str]] = defaultdict(set)

    for event in event_store.get_events():
        if event.event_type == EventType.ITEM_ADDED:
            origins[event.data.name].add(event.data.origin)

    return dict(origins)
