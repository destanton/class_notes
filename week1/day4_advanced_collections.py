#tuple is a list that cannot be changed
my_tuple = ("danielle", "helen")
print(my_tuple)
# my_tuple.append("peanut")
#print(my_tuple) doesn't work. can't appned tuples

my_string = "cell phone"
print(my_string + "s")
my_string += "s"
print(my_string)


my_set = {2, 7, 9, "danielle"}
my_people_set = {"danielle", "sarah", "peanut"}

print(my_set.intersection(my_people_set))
