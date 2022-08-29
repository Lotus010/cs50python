# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 17:12:16 2022

@author: psen
"""
import random



while True:
    try:
        Level = int(input("Level: "))
        if Level > 0:
            break
        else:
            continue
        
    except TypeError :
        continue
    

Ans = random.randint(1, Level)

while True:
    try:
        Guess = int(input("Guess: "))
        if Guess < Ans:
            print("Too small!")
        elif Guess == Ans:
            print("Just right!")
            break
        else:
            print("Too large!")
        
    except TypeError:
        continue