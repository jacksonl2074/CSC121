#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 13:48:10 2023

@author: jacksonl2074
"""


# create variable that would ref user entry




score = float(input("Enter a score (between 0 and 100 or -1 to terminate: "))

while score != -1:
    

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
        
    score = float(input("Enter a score (between 0 and 100 or -1 to terminate": ))
            