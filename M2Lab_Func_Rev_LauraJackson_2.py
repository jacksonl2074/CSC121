# -*- coding: utf-8 -*-
"""
Dollar Store, with discounts if purchasing more than 10 items
9.14.23
CSC 121 M2Lab - Function Review
Laura K. Jackson
"""
import main_m2lab               # import main?

# define calcCost function
def calcCost(count):
    
    main_m2lab.main_m2lab       # import main?
    
    count = int(input("Enter number of items: "))
    # variable for item cost
    item_cost = 1.00
    
    # decision structure for discount
    if count >= 10:
        discount = 0.95         # discount of 5% for 10 or more items
    else:
        discount = 1.00         # no discount for less than 10 items
        
    # calculations for cost, before taxes
    pretax_cost = round(count * discount * item_cost, 2)
    
    return pretax_cost


# define displayLine function, no returned result
def displayLine(label, amount):
    label = format(amount, '10,.2f')
    print(label)
    
# define display function, no returned result
def display(cost, tax):
    # call calcCost function here
    cost = calcCost()       # pre-tax cost
    
    tax = 0.075             # sales tax
    
    displayLine("Net cost: ", cost)
    displayLine("Tax: ", tax * cost)
    displayLine("After tax: ", (cost + (cost * tax))) # sales tax + net cost
    