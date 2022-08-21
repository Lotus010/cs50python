# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 22:01:32 2022

@author: psen
"""

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0.0
while True:
    try:        
        item = input("Item: ").title()
        if menu.get(item):
            total = total + menu.get(item)
            print("Total: $ {:0.2f}".format(total))
    except EOFError:
        print()
        break




'''
while True:
    try:
        item = input("Item: ").title()
        if item in menu:
            print("Total: $ {:0.2f}".format(menu[item]))
        else:
            None
    except EOFError:
        print()
        break '''
    