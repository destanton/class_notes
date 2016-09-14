
#  for loop for
for _ in range(5):
    print("i am looping")

turns = 0
while turns < 5:
    print("while looping")
    turns = turns + 1
    # turns += 1 is the same as above

choice = ""
while choice != "n":  # way of saying I want to infintely loop through this (think video games)[True]
    print(choice)
    choice = input("Do you want to loop again? Y/n ")

#  list collection similar to a string  [] takes any type of input
#  to find what you want in list you have to use location (index) -- inefficient
#  dictionary is key, value storage collection
#  d = {"name": "joel", "age": "33", "fears": "[]"}
#  d["age"] will return #33 -- more efficient way of searching for something by key (any arbitrary key).
