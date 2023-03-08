import random
import copy

coords = "75.7013962306691, 9.2067648609253654"

numbers = [8, 0, 9, 6, 7, 1, 3, 4, 2, 5]
random_order = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# create a dictionary with the numbers as keys and the random order as values
number_switch = dict(zip(numbers, random_order))

print(number_switch)

print("Coordonnees avant résolution: ", coords)

final_coords = ""

# loop over coords element
for i in coords:
    # if the element is a digit in a str format
    if i.isdigit():
        # replace the element with the value of the key
        final_coords += str(number_switch[int(i)])
    else:
        # if the element is not a digit, add it to the final coords
        final_coords += i

print("Coordonnees après résolution: ", final_coords)