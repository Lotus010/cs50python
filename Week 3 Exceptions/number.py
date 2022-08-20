# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 14:32:38 2022

@author: psen
"""



try:
    integers = int(input("What's x? "))    
except ValueError:
    print("X is not a number")
else:
    print(f"x is {integers}")
        
        