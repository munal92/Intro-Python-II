# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, current_room):
        self.current_room = current_room

    # def __str__(self):
    #     return f"(player.py): {self.current_room}"

    def move_to(self, direction):
        new_room = self.current_room.is_move(direction)

        if new_room is not None:
            self.current_room = new_room
            return True
        else:
            return False
