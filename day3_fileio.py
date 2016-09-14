

#  First way to open a file

open_file = open("data_file.txt")  # have to close a file you open, else it will be locked.
contents = open_file.readlines()  # reads file
#  print(help(open_file))
open_file.close()  # close file that was just opened.

print(contents)
#  second way to open a file (don't have to remember to close file)

with open("data_file.txt") as better_open_file:
    better_contents = better_open_file.read()
print(better_contents)

# benefit to using this allows to open, inside indentation block will keep code open, closes outisde of indentation
