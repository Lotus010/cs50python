# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 11:48:16 2022

@author: psen
"""

def main():
    x = int(input("what's x? "))
    if is_even(x):
        print("Even")
    else:
        print("odd")
'''        
def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False
'''    
def is_even(n):
    #return True if n%2==0 else False    
    return n%2==0


main()        