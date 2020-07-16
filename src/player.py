# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, current_location):
        self.current_location = current_location

    def __str__(self):
        return f"(player.py): {self.current_location}"
