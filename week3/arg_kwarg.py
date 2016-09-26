# positional arguements (ORDER MATTERS). paramters only referred to by var. names.
def adder(number_one, number_two, message="No Message Passed", happy=True):
    print(message)
    print(happy)
    return number_one + number_two

print(adder(9, 4, message="do something", happy=False))
print(adder("Joel", " likes programming"))

#  if you want to add a infinite number of positional args (come out as tuple). use *


def add(*args):  # splat a list puts it back in parameter
    return sum(args)

print(add(1, 2, 5, 7, 9, 19, 20))

print(adder(*[9, 4]))

print(add(*range(10)))  # splat breaks it out from paramter

#  if you want to splat keyword args use (come out as dict)**

# KWARGS always go to the right of positional arguments


def beginners_luck(name, account_number, *args, birthday="tomorrow", **kwargs):  # don't really want to use this much
    print(name, "NAME")
    print(account_number, "ACCOUNT NUMBER")
    print(args)
    print(kwargs)
    return 1

print(beginners_luck("Joel", 143829382, [1, 2, 3], birthday="today", lol="joel"))
