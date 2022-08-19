# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 16:11:02 2022

@author: psen
"""

#Get Input

oper = input("Enter your math expression ").split()

x = float(oper[0])
y = oper[1]
z = float(oper[2])

if y == '+':
    a=x + z    
elif y == '-':
    a = x - z
elif y == '/':
    a = x / z
elif y == '*':
    a = x * z    
        
    
print(a)    



