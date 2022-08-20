# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 12:46:16 2022

@author: psen
"""

def is_leap(year):
    leap = False
    
    if (year/4)%2 == 0:
        if (year/100)%2 == 0 :
            if (year%400)==0:
                leap = True
                return leap
        else:
            leap = True
            return leap 
         
        
    # Write your logic here
    
    return leap

year = int(input("Enter year: "))
print(is_leap(year))
#print((year/4)%2)