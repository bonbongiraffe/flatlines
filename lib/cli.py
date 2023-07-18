#!/usr/bin/env python3

if __name__ == '__main__':
    print("Welcome to Flat-lines!")
    print("- to create a new reservation, please enter: 'create' ")
    print("- to edit an existing reservation, please enter your reservation number. ")
    user_input = input('>> ')
    while user_input != "x":
        user_input = input('>> ')
        if user_input == 'create':
            pass:
