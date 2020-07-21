# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item


class Player:
    def __init__(self, current_room, inventory=[]):
        self.current_room = current_room
        self.inventory = inventory

    def move_to(self, direction):
        new_room = self.current_room.is_move(direction)

        if new_room is not None:
            self.current_room = new_room
            return True
        else:
            return False

    def inventory_list(self):
        if not self.inventory:
            print(f"inventory empty")
        else:
            for i in self.inventory:
                print(f"{i[0].item_name}")

    def add_item(self, item):
        chc = self.current_room.check_item_availability(item)
        if chc:

            itm = self.current_room.find_item(item)
            self.inventory.append(itm)
            self.current_room.remove_item(item)

    def drop_item(self, item):
        chc = [i[0]
               for i in self.inventory if item == i[0].item_name]

        # for den in chc:
        print(f"ya {chc[0].item_name} ")
        if not chc:
            print(f"item not exist in inventory")
        else:
            find_index = [index for index, i in enumerate(
                self.inventory) if item == i[0].item_name]

            print(f"{find_index[0]} ")
            del self.inventory[find_index[0]]
            self.current_room.items.append(Item(
                chc[0].item_name, chc[0].item_description))
            print(f"Succesfully deleted")
