#!/usr/bin/env python3

# Created by: Trinity Armstrong
# Created on: November 2019
# This program takes the grade level and returns the middle percentage mark


def calculate(mark):
    # This function calculates the user's grade level as a percentage mark

    # Process
    if mark == "4+":
        percentage = 98
    elif mark == "4":
        percentage = 91
    elif mark == "4-":
        percentage = 83
    elif mark == "3+":
        percentage = 78
    elif mark == "3":
        percentage = 75
    elif mark == "3-":
        percentage = 71
    elif mark == "2+":
        percentage = 68
    elif mark == "2":
        percentage = 65
    elif mark == "2-":
        percentage = 61
    elif mark == "1+":
        percentage = 58
    elif mark == "1":
        percentage = 55
    elif mark == "1-":
        percentage = 51
    elif mark == "R":
        percentage = 25
    else:
        percentage = -1
    return percentage


def main():
    # This function allows the user to input a mark and receive an outputted %

    # Input
    user_mark = input("Enter your grade level: ")

    # Process
    user_percentage = calculate(user_mark)

    # Output
    if user_percentage == -1:
        print("")
        print("Error!")
    else:
        print("")
        print("Your percentage mark is {0}%.".format(user_percentage))


if __name__ == "__main__":
    main()
