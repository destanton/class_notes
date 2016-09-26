#  MAGIC METHODS ARE STRICTLY FOR USE IN OOP

# print("Danielle" + " programs")  # string concentonations. two strings and plus operator
# print("Danielle" + 1)  # traceback is a nice word for error message


class SuperNumber:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):  # when you add two values. #converts all values to strings and smashes em together.
        # if type(self.value) == int and type(other.value) == str:
        return SuperNumber(str(self.value) + str(other.value))  # Meta create new value from the two strings and   turn into a SN.
        # print("weird string addition, giving original value")
        # return self.value
        # return "LOLOMGFAREALZ"

    def __str__(self):  # dunder str can only return a string. Anything other than will return error
        return str(self.value)  # string representation value of str. good for debug.

s_number_1 = SuperNumber(1)
s_number_2 = SuperNumber(" Danielle")
print(s_number_1)
x = s_number_1 + s_number_2 + s_number_2
#   |                     |
print(x)
