# -*- coding: utf-8 -*-

import random

def generate_one_starting_position():

    amount_of_horizontal_steps = 16
    die_sides = 3
    camels = ["W", "R", "B", "G", "Y"]
    board = []

    ### create empty board
    for i in range(1, amount_of_horizontal_steps + 3 + 1):
        board.append([" ", " ", " ", " ", " "])

    ### create starting position of camels
    ### create a copy of camels list
    copy_of_camels = camels.copy()

    for i in range(0, len(copy_of_camels)):

        ### choose random camel/color
        color_of_random_camel = random.choice(copy_of_camels)
        ### remove that element from copy of camels list
        copy_of_camels.remove(color_of_random_camel)

        roll_result = random.randint(1, die_sides)
        start_step = board[roll_result-1]

        ### find first free vertical position and place camel there
        for index, value in enumerate(start_step):
            if value != ' ':
                continue
            else:
                start_step[index] = color_of_random_camel
                break

    ### get every step of first threee steps and combine them to one list
    start_position_as_one_list = []
    for j in [0, 1, 2]:
        for item in board[j]:
            start_position_as_one_list.append(item)

    ### return combined list as tuple to be able to set this as key in a dictionary
    return tuple(start_position_as_one_list)


def main():

    ### simulate ii starting positions
    for ii in [10, 100, 1000, 10000, 100000, 1000000, 10000000]:
        dict_of_starting_positions = {}
        ### for each single simulation (jj) of all the simulations (ii) calculate the unique starting positions by adding them to a dictionary as key and count the keys
        for jj in range(0,ii):
            position = generate_one_starting_position()
            dict_of_starting_positions.get(position, 0) + 1

            if position in dict_of_starting_positions:
                dict_of_starting_positions[position] += 1
            else:
                dict_of_starting_positions[position] = 1

        #print(dict_of_starting_positions)

        print("Distinct starting positions: " + str(len(dict_of_starting_positions)) + " (" + str(ii) + " simulations of generating a starting position)")


if __name__ == '__main__':
    main()