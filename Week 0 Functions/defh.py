# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 21:37:51 2022

@author: psen
"""


def main():
    name = input("Whats your name? ").title()
    hello(name) 
    hello()   

    
def hello(to="world"):
    print("hello,", to)
    


main()    