#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 13:38:34 2023

@author: jacksonl2074
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 13:22:27 2023

@author: jacksonl2074
"""

# create variable that would ref user entry


score = float(input("Enter score: : "))

while score < 0 or score > 100:
    
    print ("INVALID ENTRY")
    print("Your score must be between 0 and 100")
    score = input("Re-enter score: ")  # this statement makes sure there is no infinite loop

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
    