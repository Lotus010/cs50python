# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 15:25:33 2022

@author: psen

Generators,Iterators,Yield
"""

def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)
    
def sheep(c):
    for i in range(c):
        yield "(+)" * i
        


if __name__ == "__main__":
    main()