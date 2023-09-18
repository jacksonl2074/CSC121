#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 14:18:48 2023

@author: jacksonl2074
"""





def main():
    print("Good afternoon")
    
    get_name()
    get_nums()

def get_name():
    
    '''
    function requests first name of user and says hi
    '''
    
    name = input("What is your name?")
    
    print("Hello, ", name)
    
    
def get_nums():
    
    '''
    function asks user to enter 2 numbers
    then adds the number and diplays results
    '''
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second  number: "))
    
    print("Total is ", num1+num2)
    
main()