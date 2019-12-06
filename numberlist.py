#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: December 2019
# This program adds 10 numbers to an array then calculates the average


import random


def main():
    # This function adds 10 numbers to an array then calculates the average

    # Variables and arrays
    average = 0
    number_array = []

    # Process
    for counter in range(10):
        number = random.randint(1, 100)
        number_array.append(number)
        print(number_array[counter])
        average = average + number_array[counter]

    average = average/10

    # Output
    print("")
    print("The average of the random numbers is", average)


if __name__ == "__main__":
    main()
