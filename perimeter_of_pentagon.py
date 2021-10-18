#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: Oct 2021
# This is the Perimeter of Pentagon program in Python

import math


def calculate_perimeter_of_pentagon(side):
    # this progam cacluates the perimeter of a pentagon

    # process
    perimeter = round(side * 5, 2)

    return perimeter


def main():
    # this function gets the legth of one side of the pentagon

    # tell the user what this program does
    print("This program calculates the perimeter of a pentagon.")

    # input
    side = input("Enter the length of one side of the pentagon: ")
    print("")

    try:
        # convert string to float
        length_of_side = float(side)  # length of only one side
        # call functions
        returned_perimeter = calculate_perimeter_of_pentagon(length_of_side)
        # output
        print("The perimeter of this pentagon is {0} cm.".format(returned_perimeter))
    except Exception:
        print("{} is an invalid input.".format(side))
    print("\nDone.")


if __name__ == "__main__":
    main()
