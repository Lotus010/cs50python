# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 14:15:08 2022

@author: psen
Doctring
Hints
"""

def meow(n : int) -> str:  #HINT
    """                            #DOCSTRING
    Meow n times
    
    :type n:int
    :raise Typererror: if n is not int
    :return: A string of meows multiplied by n
    :rtype: str
    
    """
    return "meow \n" * n

number : int = int(input("Number: "))   #HINT

Meows : str = meow(number)      #HINT

print(Meows, end="")