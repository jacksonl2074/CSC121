# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 21:17:12 2023

@author: lkjac

Program asks user to input highest temperature for each month of the year
then program calculates the average temp and displays highest and lowest temps.
10.4.23
CSC 121 M3HW3 - Lists
Laura K. Jackson
"""
def get_temp():
    
    '''
    Gets user input of temps for each month.
    Returns tempsList
    '''
    
    # create an empty list
    tempsList = []
    janTemp = float(
        input("Please enter the highest recorded temperature for January: "))
    febTemp = float(
        input("Please enter the highest recorded temperature for February: "))
    marTemp = float(
        input("Please enter the highest recorded temperature for March: "))
    aprTemp = float(
        input("Please enter the highest recorded temperature for April: "))
    mayTemp = float(
        input("Please enter the highest recorded temperature for May: "))
    junTemp = float(input("Please enter the highest recorded temperature for June: "))
    julTemp = float(input("Please enter the highest recorded temperature for July: "))
    augTemp = float(input("Please enter the highest recorded temperature for August: "))
    sepTemp = float(input("Please enter the highest recorded temperature for September: "))
    octTemp = float(input("Please enter the highest recorded temperature for October: "))
    novTemp = float(input("Please enter the highest recorded temperature for November: "))
    decTemp = float(input("Please enter the highest recorded temperature for December: "))
    
    tempsList = [janTemp, febTemp, marTemp, aprTemp, mayTemp, junTemp, julTemp, 
                 augTemp, sepTemp, octTemp, novTemp, decTemp]
    
    
    # list with month names and variables representing temps
    matrix = [['January', janTemp], ['February', febTemp], ['March', marTemp],
              ['April', aprTemp], ['May', mayTemp], ['June', junTemp],
              ['July', julTemp], ['August', augTemp], ['September', sepTemp],
              ['October', octTemp], ['November', novTemp], ['December',
                                                            decTemp]]
    
    # print(tempsList)
    print("\nFayetteville, NC 2022 Temp\n")
    print("--------------------------\n")
    
    
    # print info as a table
    
    for row in matrix:
        for cell in row:
            # print(cell, end=' ')
            print(f'{cell:<15}', end= ' ')
        print()
        
    print("--------------------------\n")
    
    return tempsList

def main():
    '''
    This is the main function. After gathering temps in the get_temp function
    the average temp is calculated and displayed, along with the highest and 
    lowest temps.
    
    Returns
    -------
    None.

    '''
    print("Welcome to the Temperature program!\n")

    # call get_temp function
    tempsList = get_temp()      # should I change variable name? FIXME

    # use min and max methods to access lowest/highest temps
    highTemp = max(tempsList)
    lowestTemp = min(tempsList)
    
    # average temp for year using sum and len methods
    avgTemp = sum(tempsList)/ len(tempsList)
    
    # print out results
    print("Highest Temp: ", highTemp)
    print("Lowest Temp: ", lowestTemp)
    print("Average temp: ", round(avgTemp,1))
    

if __name__ == "__main__":
    main()
