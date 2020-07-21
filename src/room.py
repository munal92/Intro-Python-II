# Implement a class to hold room information. This should have name and
# description attributes.
from player import Player


class Room:
    def __init__(self, room_name, description, n_to=None, e_to=None, s_to=None, w_to=None, items=[]):
        self.room_name = room_name
        self.description = description
        self.n_to = n_to
        self.e_to = e_to
        self.s_to = s_to
        self.w_to = w_to
        self.items = items

    def item_list(self):
        if not self.items:
            print(f"Empty!")
        else:
            for i in self.items:
                print(f"{i.item_name} -> {i.item_description}")

    # def __str__(self):
    #     return f'{self.items}'

    def is_move(self, direction):
        if direction == 'n':
            return self.n_to
        elif direction == 'e':
            return self.e_to
        elif direction == 'w':
            return self.w_to
        elif direction == 's':
            return self.s_to
        else:
            return None

    def check_item_availability(self, check_item):
        room_inv = [i.item_name for i in self.items]
        if not self.items:
            print("Room is empty!")
            return False
        elif check_item in room_inv:

            print(f"Succesfully picked {check_item}")
            return True
        else:
            print("Item is not exist!")

    def remove_item(self, remove_item):
        room_inv = [index for index, i in enumerate(
            self.items) if i.item_name == remove_item]
        room_inv2 = [i.item_name for i in self.items]
        if remove_item in room_inv2:
            del self.items[int(room_inv[0])]
            print(f"removed: {remove_item}")

    def find_item(self, itm):
        room_inv = [i for i in
                    self.items if i.item_name == itm]

        if room_inv:
            return room_inv

    def add_item_rm(self, item):
        self.items.append(item)
