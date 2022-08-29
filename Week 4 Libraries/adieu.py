# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 16:30:26 2022

@author: psen
"""

import inflect

p = inflect.engine()

word = []

while True:
    try:
        w = input("Name: ")
        word.append(w)
    except EOFError:
        print()
        break
    
s = p.join(word)

print("Adieu, adieu, to " + s)    