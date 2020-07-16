from room import Room
from player import Player
from os import system, name
from time import sleep
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
#
# Main
#

# Make a new player object that is currently in the 'outside' room.


player = Player(room['outside'])
directions = ["n", "e", "w", "s"]

# Write a loop that:
#
# * Prints the current room name
print(
    f"\nYou're in {player.current_room.room_name}\nand it's {player.current_room.description}\n")

while True:

    # * Prints the current description (the textwrap module might be useful here).
    direction_input = input(
        "Which direction would you like to go? (N,E,W,S)\n").strip().lower().split()[0]
    sleep(1)
    clear()
    direction_input = direction_input[0]
    if direction_input == 'q':
        break

    if direction_input in directions:
        is_valid = player.move_to(direction_input)
        if is_valid:
            print(
                f"Entered to {player.current_room.room_name} and it's {player.current_room.description}\n")
        else:
            print(f"You can't move to that direction try something else: ")
    else:
        print(f"Please Enter a Valid Direction {direction_input}\n")

    # sleep(5)
    # clear()
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# gameplay loop
