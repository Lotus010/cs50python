# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 21:58:17 2022

@author: psen
"""

def main():
    x= int(input("Input a number to be squared "))
    print("Your number is now squared ", square(x))
    
def square(num):
    return pow(num,2)

main()    