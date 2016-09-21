# Inventory Tracker RPG
# Player that has attributes
# Inventory
# Items

player = {"inventory": {"red potion": {"quantity": 20}}}
{
    "red potion": {
        "quantity": 1
    }
}

player_name = input("Welcome Traveler! What is your name? ")
player["name"] = player_name
print(player)

# want to start from the inside out when improving (refactoring) the code

while True:
    choice = input("Would you like to (i)nspect your inventory? or (a)dd to your inventory?\n>")
    if choice == 'a':
        print("adding item to inventory")
        item_name = input("What is the item name? ")
        item_quantity = int(input("How many? "))
        player["inventory"][item_name] = {"quantity": item_quantity}
    elif choice == 'i':
        print("looking at inventory")
        for item in player["inventory"].keys():
            quantity = player["inventory"][item]["quantity"]
            print("{} - {}".format(item, quantity))
