from room import Room
from player import Player
from item import Item
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


# room['outside'].items = Item("Sword", "Steel Sword")
# room['outside'].items = Item("Helmet", "Helmet 100+")
# room['foyer'].items = Item("Knife", "Steel Knife")
# room['narrow'].items = Item("Pistol", "9mm Pistol")


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
player_inventory = []

room['outside'].items = [
    Item("Sword", "Steel Sword"), Item("Helmet", "Helmet 100+")]
room['foyer'].items = [Item("Knife", "Steel Knife")]
room['narrow'].items = [Item("Pistol", "9mm Pistol")]

# Write a loop that:
#
# * Prints the current room name
print(
    f"\nYou're in {player.current_room.room_name}\nand it's {player.current_room.description}\n\nRoom Items List:")
player.current_room.item_list()
# print("\nPlayer Inventory: ")
# player.inventory_list()
# print()
while True:

    # * Prints the current description (the textwrap module might be useful here).
    print("\nPlayer Inventory: ")
    player.inventory_list()
    print()
    direction_input = input(
        "Which direction would you like to go? Or you can pick up or drop off items\nEnter:\nTo move --> (N,E,W,S)\nTo get/drop item/check inventory --> i\nTo Quit --> q\nEnter here: ").strip().lower().split()[0]

    direction_input = direction_input[0]
    if direction_input == 'q':
        break
    elif direction_input == 'i':
        print(f"\n****\nWelcome to Store!\nRoom Items List:")
        player.current_room.item_list()
        inv_input = input(
            f"You can pick up or drop off items. Simlpy type drop get [ITEM_NAME] or [ITEM_NAME]\nEnter Here:").strip().title().split()
        if inv_input[0] == 'Get':
            # print(f"\n Picked item: {inv_input[1]}")
            # player.current_room.check_item_availability(inv_input[1])
            # player.current_room.remove_item(inv_input[1])
            player.add_item(inv_input[1])
        elif inv_input[0] == 'Drop':
            player.drop_item(inv_input[1])
            #  print(f"\n Dropped item: {inv_input[1]}")
        elif inv_input[0] == 'Q':
            continue
        else:
            print(f"\n Invalid command! {inv_input[0]} {inv_input[1]}")

        print(f"\n****")
    elif direction_input in directions:
        is_valid = player.move_to(direction_input)
        if is_valid:
            print(
                f"\n**\nEntered to {player.current_room.room_name} and it's {player.current_room.description}\n\nRoom Items List:")
            player.current_room.item_list()
            print()
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
