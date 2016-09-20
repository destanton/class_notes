import csv  # importing module from python library.
with open("data.csv") as in_file:  # important that this is a string
    contents = in_file.readlines()  # read is good for "reading" in an entire list of text, like a book
# print(contents[2].split(","))  # readlines takes every line of the file and puts it in its own row.

clean_data = []

# for row in contents:  # going to iterate over each row
#     row = row.replace("\n", "")
#     clean_data.append(row.split(","))  # splitting the row on the comma and appending it to clean_data

clean_data = [row.replace("\n", "").split(",") for row in contents]

# print(clean_data[11][4])
# print(clean_data)

with open("data.csv") as in_file:
    # contents = csv.reader(in_file) # delimiter="|" if data was split by some other item, have to do add this.
    contents = csv.DictReader(in_file)  # delimiter="|" # dict reader allows column access by name
    print(list(contents)[1])  # ["Water Temp"]

# Modules import
# way 1 -- from random input randint (as joel_random)// x = randint(1, 20)
# way 2 -- import random // x = random.randint(1, 20)
# way 3 -- from random import * // x = randint(1, 20) worst way to do it. Uncle brings all the jokes

# Datetime - a way to do a lot of date work, details in python.
# serialize - convert from a basic type (str) to a complex type (date/datetime object)
