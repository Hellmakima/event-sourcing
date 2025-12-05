from inventory import Inventory
from event_store import EventStore
from item import Item
from projections import get_most_collected_items, get_item_origins

def main():
    event_store = EventStore()
    inventory = Inventory(event_store)

    item1 = Item("item1", "rare", "origin1")
    item11 = Item("item1", "rare", "next_origin")
    item2 = Item("item2", "common", "origin2")
    item3 = Item("item3", "rare", "origin3")
    item4 = Item("item4", "common", "origin4")

    inventory.add_item(item1)
    inventory.add_item(item11)
    inventory.add_item(item1)
    inventory.add_item(item1)
    inventory.add_item(item2)
    inventory.add_item(item3)
    inventory.add_item(item3)
    inventory.add_item(item3)
    inventory.add_item(item4)
    inventory.remove_item(item3)
    inventory.remove_item(item3)
    inventory.remove_item(item3)
    try:
        inventory.remove_item(item3)
    except Exception as e:
        print(e)

    print(inventory.get_items())
    print(inventory.get_count(item3))
    print(get_most_collected_items(event_store))

    print(get_item_origins(event_store))

if __name__ == "__main__":
    main()