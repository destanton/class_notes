# Inventory Tracker RPG
# Player that has attributes
# Inventory
# Items

player = {}
player_name = input("Welcome Traveler! What is your name? ")
player["name"] = player_name
print(player)

choice = input("Would you like to (i)nspect your inventory? or (a)dd to your inventory?\n>")

while True:
    if choice == 'a':
        print("adding item to inventory")
    elif choice == 'i':
        print("looking at inventory")
