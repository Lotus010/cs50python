# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 11:59:04 2022

@author: psen
"""

name = input("What's the name? ").title()

'''
if name == "Ron" or name == "Hermoine" or name == "Harry":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
'''

match name:                 #noqa
    case "Harry":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Hermoine":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")