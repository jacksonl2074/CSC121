#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 13:22:27 2023

@author: jacksonl2074
"""

# create variable that would ref user entry

keep_going = "y"

while keep_going.lower() == 'y' or keep_going.lower() == 'yes':
    score = float(input("Enter score: : "))
    
    #evaluate the score
    
    if score >=90 :
        
        print ("A")
        
    elif score >=80:
        
        print("B")
        
    elif score >=70:
        
        print("C")
        
    elif score >=60:
        
        print("D")
        
    else:
        print("F!")
        
    keep_going = input("Do you want to enter another score? (y for yes)")
        