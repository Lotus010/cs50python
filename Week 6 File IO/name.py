# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 17:20:51 2022

@author: psen
"""
'''
names = []

file = open("names.txt","a")
for _ in range(3):
    name = input("What's your name? ")
    names.append(name)
    file.write(f"{name}\n")
    
#for name in sorted(names):
#    print(f"hello, {name}")
    
file.close()    
'''
names = []
with open("inames.txt","a") as file:
    for _ in range(3):
        name = input("What's your name? ")
        names.append(name)
     
    for name in sorted(names):
        file.write(f"{name}\n")