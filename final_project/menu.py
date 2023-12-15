# -*- coding: utf-8 -*-
"""
Final Project: Course information saved into a csv file, printed to user on
console, and uses OOP.
CSC 121-0002
Laura K. Jackson
12.15.23
"""
# imports
import functions as fn

# Constants for the menu choices

ENTER_COURSES = 1
DISPLAY_COURSES = 2
RETRIEVE_INFO_COURSE = 3
QUIT_CHOICE = 4

# The main function
def main():

    # The choice variable controls the loop
    # and hold the user's menu choice

    choice = 0

    while choice != QUIT_CHOICE:

        # display menu
        display_menu()

        # get user's choice
        choice = int(input("Enter your choice: "))

        # Perform the calculation selected
        if choice == ENTER_COURSES:

            fn.enter_Course()

        elif choice == DISPLAY_COURSES:
            
            fn.display_Courses()

        elif choice == RETRIEVE_INFO_COURSE:

            fn.retrieve_Info()

        elif choice == QUIT_CHOICE:
            print("\nExiting the program.......")

        else:
            print("\nError: Invalid Entry")
            print("Please enter a choice between 1-4.")




# display menu options
def display_menu():

    print('\n MENU')
    print('-'*45)
    print("1)  Enter list of courses you registered in")
    print("2)  Display list of courses you registered in")
    print("3)  Retrieve information on one of your courses")
    print("4)  Quit")
    print('-'*45)

if __name__ =="__main__":
    main()