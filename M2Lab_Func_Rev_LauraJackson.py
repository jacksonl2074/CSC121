# -*- coding: utf-8 -*-
"""
Dollar Store, with discounts if purchasing more than 10 items
9.14.23
CSC 121 M2Lab - Function Review
Laura K. Jackson
"""

import function_m2lab as calcCost

def main():      # menu for user to select a choice 
    print("Menu")
    print("1. Enter number of items: ")
    print("2. Quit")
    print()
      
    choice = input("Enter your choice: ")

    
    if choice == '1':
        print("dollar store function")
        
        count = int(input("Enter number of items: "))
        calcCost()
        
    elif choice == '2':
        print("Exit program")
    else:
        print("invalid choice")
        # add a loop to make a valid choice?
        
# call to main()        
main()


