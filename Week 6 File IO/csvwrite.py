# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 16:45:24 2022

@author: psen
"""

import csv

name = input("What's your name? ")
home = input("What's your home? ")
'''
with open("writes.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name,home])
'''    
with open("writes.csv", "a", newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["name","home"])
    writer.writerow({"home":home,"name":name})
        