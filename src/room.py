# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, room_name, description, n_to=None, e_to=None, s_to=None, w_to=None, items=None):
        self.room_name = room_name
        self.description = description
        self.n_to = n_to
        self.e_to = e_to
        self.s_to = s_to
        self.w_to = w_to

    # def __str__(self):
    #     return f"Current location: {self.room_name}\nDescription: {self.description}\n "

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
