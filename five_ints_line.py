#!/usr/bin/env python3
# Created by: Remy Skelton
# Created on: Nov 21, 2023
# This program will display all umbers from 1000 to 2000
# and skip line every 5 digits with if inside the loop


def main():
    # display message about program
    print("This program will display all numbers from 1000 to 2000")
    print("and skip line every 5 digits.")

    # for loop to display all the numbers between 1000 and 2001
    for counter in range(1000, 2001):
        # if to skip lines when needed
        if counter == 1000:
            print(f"{counter}, ", end="")
        elif counter % 5 == 0:
            print("")
            print(f"{counter}, ", end="")
        else:
            print(f"{counter}, ", end="")


if __name__ == "__main__":
    main()
