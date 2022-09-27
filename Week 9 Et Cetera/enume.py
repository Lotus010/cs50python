# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 14:16:58 2022

@author: psen
"""

students = ["Hermoine","Harry","Ron"]

for i,student in enumerate(students):
    print(i+1, student)
    
#Enumerate list of tuples in order    
print(list(enumerate(students))) 