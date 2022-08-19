# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 10:02:28 2022

@author: psen
"""

#Declare value of c
c= 300000000

#Ask users Mass as input and convert to int
M = int(input("Enter your mass(in kg) to calculate the energy in joules "))



#Calculate Energy
E = M *c**2

#Print Energy
print(f"{E} joules")
#print(E,end=" ")
#print("joules")