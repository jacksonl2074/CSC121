#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 14:21:07 2023

@author: jacksonl2074
"""

keep_going = 'y'

init_amount = float(input("Enter starting amount in account: $"))
# while init_amount <= 0:
    # print("Amount must be greater than 0.")

expenses = 0

remain_amount = init_amount

while keep_going == 'y':
    

    expenses +=1
    expense = float(input("Enter expense " + str(expenses)+": "))
  
    # subtract
    remain_amount = remain_amount - expense # remain_amount -= expense
    
    keep_going = input("Do you want to enter another expense? ")
    
print("Initial amount: ", init_amount)

print("Expenses enter: ", expenses)
print("Remaining amount: ", remain_amount)
    1

