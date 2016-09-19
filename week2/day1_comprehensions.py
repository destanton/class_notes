#  For loop way
l = [4, 1, 11, 13] #  convert age to dog years
age = []
for person in l:
    petyears = person * 7
    age.append(petyears)
print(age)

#  comprehension way (condensed version of a for loop that will make a list)
L = [4, 1, 11, 13]
ages = [person*7 for person in L]
#  numbres smaller than 10
# age = [person*7 for person in L if person<10]

list_of_numbers = [9, 10, 5, 100, 23, 2]

half_values = []

for number in list_of_numbers:
    half_of_x = number / 2   #  / true division  // floor division (round down to nearest integer)
    half_values.append(half_of_x)
print(half_values)

##################################################################

list_of_numbers = [9, 10, 5, 100, 23, 2]
half_values = [number / 2 for number in list_of_numbers]
print(half_values)


## half_values = tuple(number / 2 for number in list_of_numbers)


####################################################################
## Dictionary comprehension - can add/edit keys and values on the fly
## - bloated way
list_of_numbers = [100, 67, 23, 45, 11]
square_numbers = {}
for number in list_of_numbers:
    square_numbers[number] = number ** 2

print(square_numbers)


####################################################################
#  Dict comprehension way

list_of_numbers = [100, 67, 23, 45, 11]
square_numbers = {number: number ** 2
                  for number in list_of_numbers}
print(square_numbers)

####################################################################
#  matrix is a list of lists

matrix = [["_", "X", "_"],
          ["O", "X", "O"],
          ["O", "X", "O"]]
print(matrix[1])

#  nested iteration
for row in matrix:
    for column in row:
            print(column)

target_column = []
for row in matrix:
    target_column.append(row[1])
print(target_column)

####################################################################
matrix = [["_", "X", "_"],
          ["O", "X", "O"],
          ["O", "X", "O"]]
target_column = [row[1] for row in matrix]
print(target_column)

####################################################################
