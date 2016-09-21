import sys
import random

lines = ["joel", "peanutz", "sarah", "rocket", "python", "supercatmagicexpertallioucious"]
comp_word = "ruby"
mode_choice = input("give me input! (e/n/h) ")

def word_game(word):
    print(word)
    quit = input("quit? ")
    if quit:
        sys.exit()
    print("in word game")

high_range = 6
low_range = 0

if mode_choice == 'e':
    high_range = 6
    low_range = 0
if mode_choice == 'n':
    high_range = 10
    low_range = 6
if mode_choice == 'h':
    high_range = 100
    low_range = 10

while True:
    random_word = comp_word
    if len(random_word) > low_range and len(random_word) <= high_range:
        word_game(random_word)
    else:
        comp_word = random.choice(lines).lower().replace("\n", "")
