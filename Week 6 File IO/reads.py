# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 17:40:42 2022

@author: psen
"""
'''
with open("names.txt","r") as file:
    lines = file.readlines()
    
for line in lines:
    #print("hello ",line,end = "") 
    print("hello ",line.rstrip()) 
'''    
with open("names.txt","r") as file:
    for line in file:
        print("hello,",line.rstrip())
        
with open("inames.txt","r") as file:
    for line in sorted(file):
        print("hello,",line.rstrip())
                
        
        