# input 1 = "programming is fun"
# input 2 = "m"
# output = [6, 7]

sentence = "i decided to learn how to program and it was a good decision"
letter = " "
output = []

# current_location = 0



# for current_letter in sentence:
#     if current_letter == letter:
#         output.append(current_location)
#     current_location += 1

# enumerate provides location of where a letter currently is

for current_location, current_letter in enumerate(sentence):
    if current_letter == letter:
        output.append(current_location)



# print(sentence.index(letter))  #  useful but only for first occurance


print(output)


my_list = ["danielle", "helen", "riley", "oliver"]
print(my_list)
enumerate(my_list)
list(enumerate(my_list))
print(list(enumerate(my_list)))

for x, y in list(enumerate(my_list)):
    print("{} {}".format(x, y))
