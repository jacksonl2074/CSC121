# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 18:32:28 2023

@author: lkjac


"""
from course import Course
import csv

def enter_Course():
    
    '''
    This function allows the user to enter in various information regarding
    courses and saves it to a CSV file.
    '''
    
    try:
    
        # empty list to save instances
        accounts = []
        
        classes = int(input("Enter number of classes you are registered for: "))
        
        # for loop to iterate through num of courses user enters, get info
        for account in range(1, classes+1):
            code = input("Enter course code (ex: CTI110): ")
            section = input("Enter course section (ex: 0001): ")
            name = input("Enter course name (ex: 'Intro to Programming'): ")
            days = input("Enter days course meets (or online): ")
            start = input("Enter course start time (ex: 9:00am): ")
            end = input("Enter course end time (ex: 11:00am): ")
            location = input("Enter course location (ex: ATC 155): ")
            
            # create instances
            student_courses = Course(code, section, name, days, start, end, location)
            
            # save instances in a list
            accounts.append(student_courses)
        
        # write info to a CSV file    
        with open("courseInfo.csv", "w", newline='') as inFile:
            
            # create csv writer object
            csvFile = csv.writer(inFile)
            csvFile.writerow(['Course Code', 'Course Section', 'Course Name', \
                              'Days', 'Start Time', 'End Time', 'Location'])
            for account in accounts:
                csvFile.writerow([account.get_code(), account.get_section(), \
                                  account.get_name(), account.get_days(),\
                                      account.get_start(), account.get_end(), \
                                          account.get_location()])
    except FileNotFoundError:
        print("\nThe file cannot be file. Must register for classes.")
        
    except:
        print("/nError.")
        
    return accounts

def display_Courses():
    '''
    This function displays all course information to user. Output to screen
    console.
    '''
    
    try:
    
        # create empty list to store instances later on
        accounts = []
        
        # open CSV file
        inFile = open("courseInfo.csv", "r")
        
        inFile.readline()

        # header row fields
        # NOTE: tried to format this header row and I can't get it to format
        # in a nice way. This goes for line 82 as well.
        headerRow = f'{"Course Code":<20}{"Section":<10}{"Name":<15}{"Days":<10}\
            {"Start":<6}{"End":<6}{"Location":<10}'
    
        print(headerRow)
        
        # iterate over lines in file to display to user
        for row in inFile:
            
            code, section, name, days, start, end, location = row.split(",")
            
            # create instances
            student_courses = Course(code, section, name, days, start, end, location)
            
            # save instances in a list
            accounts.append(student_courses)
            
            # print info to screen/show user
            print(f'{code:<20}{section:<10}{name:<15}{days:<10}{start:<6}{end:<6}{location:<10}')
        
        # close file
        inFile.close()
        
    except FileNotFoundError:
        print("You have not registered for classes at this time.")
        
    except:
        print("\n Error.")
        
    

def retrieve_Info():
    
    '''
    This function asks the user to enter in a course code (ex.: CTI 110), and
    if it is stored in the CSV file (created in first function), then it will
    print out the info requested. Otherwise, it will tell the user they have
    not yet registered for classes.
    '''
    
    try:
        # create empty list to store instances later on
        accounts = []
        
        # open file
        inFile = open("courseInfo.csv", "r")
        
        # search for course code 
        search = input("Enter course code: ")
        
        # skips over header row in CSV file
        inFile.readline()
    
        # iterate over rows in file to extract info
        for row in inFile:
            
            code, section, name, days, start, end, location = row.split(",")
            
            # create instances
            student_courses = Course(code, section, name, days, start, end, location)
            
            # save instances in a list
            accounts.append(student_courses)
            
        # close file
        inFile.close()
        
        
        # for loop to iterate over list of student courses (accounts)
        # if found in file, print out course info to user
        for account in accounts:
            
            if account.get_code() == search:
                
                print(account)
            if account.get_code() != search:
                print("You need to register for courses.")


    except FileNotFoundError:
        print("Registration file does not exist.\nYou must register for \
              classes.")
              
    except:
        print("an error has occurred.")
    
