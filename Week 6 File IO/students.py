# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 18:08:39 2022

@author: psen
"""

with open("students.csv") as file:
    for line in file:
        #row = line.rstrip().split(",")
        #print(F"{row[0]} is in house {row[1]}")
        name, house = line.rstrip().split(",")
        print(F"{name} is in house {house}")
        
        