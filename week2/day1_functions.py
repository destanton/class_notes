# Function, a way of encapsulating logic.
# input as parameters, output as return values
# Inside () is a "method signature"


def square(number):
    return_value = number ** 2
    print("We got the value!")
    return return_value
print(square(94))


# parameter is inside the () (method signature). It's also inside the function definition. generic description
#  argument is in the () in the x = . Like a concrete value.
#  Want to have the same number of arugments as parameters.

def add(left, right):
    return left + right

print(add(1000, 2000))
