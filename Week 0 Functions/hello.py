# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 17:34:04 2022

@author: psen
"""
#Ask user for the name
name = input("What's your name? ").strip().title()

#Remove Whitespaces
#name = name.strip().title()

#Capitalise the Name
#name = name.capitalize()
#name = name.title()


#Say hello to User
#print ("hello,",name,sep="???")
#print("hello,",end = " ")
#print(name)

#split users name on space
first,last = name.split(" ")

print(f"hello, {first}")
