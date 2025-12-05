from event_store import EventStore
from event import Event, EventType
from collections import Counter
from functools import cache
from item import Item

class Inventory:
    def __init__(self, event_store: EventStore[Item]) -> None:
        self._event_store = event_store

    def add_item(self, item: Item) -> None:
        event = Event(event_type=EventType.ITEM_ADDED, data=item)
        self._event_store.append(event)
        self._invalidate_cache()

    def _invalidate_cache(self) -> None:
        self.get_items.cache_clear()

    @cache
    def get_items(self) -> list[tuple[str, int]]:
        counts = Counter[str]()
        for event in self._event_store.get_events():
            item_name = event.data.name
            if event.event_type == EventType.ITEM_ADDED:
                counts[item_name] += 1
            elif event.event_type == EventType.ITEM_REMOVED:
                counts[item_name] -= 1
        return [
            (item, item_count) for item, item_count in counts.items() if item_count > 0
        ]

    def get_count(self, item: Item) -> int:
        # counts = 0
        # for event in self._event_store.get_events():
        #     if event.event_type == EventType.ITEM_ADDED:
        #         if event.data["item_id"] == item_id:
        #             counts += event.data["quantity"]
        #     elif event.event_type == EventType.ITEM_REMOVED:
        #         if event.data["item_id"] == item_id:
        #             counts -= event.data["quantity"]
        # return counts
        return dict(self.get_items()).get(item.name, 0)

    def remove_item(self, item:Item) -> None:
        if self.get_count(item) <= 0:
            raise ValueError(f"Item [{item}] not present in inventory")
        event = Event(EventType.ITEM_REMOVED, item)
        self._event_store.append(event)
        self._invalidate_cache()