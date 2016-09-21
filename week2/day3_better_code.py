# Inventory Tracker RPG
# functions should only change variables given, or that they create themselves.


def add_item_to_inventory(player):  # taking the player argument from above
    item_name = input("What is the item name? ")
    item_quantity = int(input("How many? "))
    # pass  # makes prograom go to the next line of code
    # is item already in inventory?
    # if it is, just add quantity, don't replace
    if item_name in player["inventory"].keys():
        player["inventory"][item_name]["quantity"] += item_quantity
    else:
        # ADDING BRAND NEW ITEM TO INVENTORY W/ QUANTITY
        player["inventory"][item_name] = {"quantity": item_quantity}
# mutating player dictionary by side effect.
# want to start from the inside out when improving (refactoring) the code
# if calling function and not assiging to a variable, a RETURN is unnecessary


def inspect_inventory(player):
    for item in player["inventory"].keys():
        quantity = player["inventory"][item]["quantity"]
        print("{} - {}".format(item, quantity))


def player_input(player, choice):
    if choice == 'a':
        add_item_to_inventory(player)
    elif choice == 'i':
        inspect_inventory(player)


def make_character():
    player = {"inventory": {"red potion": {"quantity": 20}}}
    player_name = input("Welcome Traveler! What is your name? ")
    player["name"] = player_name
    return(player)
################################################################

player = make_character()

while True:
    choice = input("Would you like to (i)nspect your inventory? or (a)dd to your inventory?\n>")
    player_input(player, choice)
