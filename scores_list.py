#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 13:13:24 2023

@author: jacksonl2074
"""

'''
ask the user for number of scores they want to enter

create an empty list to reference the scores

in separate function (get_scores)

start a loop that asks user to enter a score and add
it to list of scores

the function is to return populated list of scores

after collecting scores, calculate score average, then display score average
'''


import nums_main_funct as nm

def main():
    
    nm.get_name()
    # ask the user for number of scores they want to enter
    score_num = int(input("Enter number of scores: "))
    
    # create an empty list to reference the scores
    scores = []                             # or scores = list() 
    
    # call get_scores
    scores = get_scores(scores, scoreNum)  # from return statement in get_scores fxn
    
    # after collecting scores, calculate score average, then display score average
    avg = sum(scores)/len(scores)        # sum(scores)/scoreNum
    
    print("Average scores is:",avg)
    
    
def get_scores(scores, numOfScores):
    '''
    function requires two arguments, one referencing empty list, and
    another referencing number of scores
    
    start a loop that asks user to enter a score and add
    it to list of scores
    '''
    
    for x in range(numOfScores):        # x can be i or num
        score = float(input("Enter score: "))
        scores.append(score)

    return scores
    
    
if __name__ == "__main__":
    main()
    



