from inventory import Inventory
from event_store import EventStore
import json
from item import Item

def main():
    event_store = EventStore()
    inventory = Inventory(event_store)

    item1 = Item("item1", "rare", "origin1")
    item2 = Item("item2", "common", "origin2")
    item3 = Item("item3", "rare", "origin3")
    item4 = Item("item4", "common", "origin4")

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

    # print(json.dumps(inventory.get_items(), indent=2))
    print(inventory.get_items())
    print(inventory.get_count(item3))

if __name__ == "__main__":
    main()