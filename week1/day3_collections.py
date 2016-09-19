
my_string = "peanut is awesome"
my_string = my_string.split()
# convert large string into list of occurances. .split will make inv. words inside a list.
print(my_string)
my_list = ["danielle", 29, ["falling", "bees"]]

#  lists always retain the order of input
print(my_list)
#  prints order and synntax
my_list.append("riley")  # add item to the end of a list
print(my_list)
my_list.pop()  # when you pop something (from the right) it moves items over (changes index)
print(my_list)
print(my_list[1])
print(my_list[2])
print(my_list[2][1])  # prints list, index two (which is a list), and then the index of that list.

my_dict = {
    "name": "danielle",
    "age": "29",
    "fears": ["falling", "wasps"]
}  # there is no perfect data structure. There are times for both lists and dicts.

print(my_dict["name"])
print(my_dict["age"])
print(my_dict["fears"])

#  print(dir(my_list))  # dir allows you to see what you can do with the variable passed in.
#  print(help(my_list))  # help lets you know what you can do to your variable.
#  navigate help with j and k, or up and down arrow
#  print(help(my_dict))
#  print(my_dict.values())
#  print(my_dict.keys())
