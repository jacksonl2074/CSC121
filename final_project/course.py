# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 20:59:46 2023

@author: lkjac
"""

class Course:
    '''
    Class Course has 7 attributes: code, section, name, days, start, end,
    location. 
    '''
    
    
    def __init__(self, code, section, name, days, start, end, location):
        
        self.__code = code
        self.__section = section
        self.__name = name
        self.__days = days
        self.__start = start
        self.__end = end
        self.__location = location
        
        
    def __repr__(self):
        
        
        return f'Course Code : {self.__code}\tSection : {self.__section}\tCourse Name \
            : {self.__name}\tDays: {self.__days}\tStart: {self.__start}\t \
                End: {self.__end}\tLocation: {self.__location}'
    
    # setters
    def set_code(self, new_code):
        self.__code = new_code
        
    def set_section(self, new_section):
        self.__section = new_section
        
    def set_name(self, new_name):
        self.__name = new_name
        
    def set_days(self, new_days):
        self.__days = new_days
        
    def set_start(self, new_start):
        self.__start = new_start
        
    def set_end(self, new_end):
        self.__end = new_end
        
    def set_location(self, new_location):
        self.__location = new_location
    
    # getters
    def get_code(self):
        
        return self.__code
    
    def get_section(self):
        
        return self.__section
    
    def get_name(self):
        
        return self.__name
    
    def get_days(self):
        
        return self.__days
    
    def get_start(self):
        
        return self.__start
    
    def get_end(self):
        
        return self.__end
    
    def get_location(self):
        
        return self.__location
    
# testing out repr print statements
# testing out program/triggering repr to print out info
code = "CTI 110"
section = "0002"
name = "Intro to Programming"
days = "m/w"
start = "9:00am"
end = "10:50am"
location = "ATC 156"

person1 = Course(code, section, name, days, start, end, location)
# print(person1)