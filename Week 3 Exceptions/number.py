# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 14:32:38 2022

@author: psen
"""

#Handling Exception
#ValueError - Entered value is not type int

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")
    
def get_int(prompt):
    while True:
        try:
            #integers = int(input("What's x? "))
            return int(input(prompt))         
        except ValueError:
            print("X is not a number")
        #else:
        #    return integers
        

if __name__ == "__main__":
    main()
        

    
#NameError - When int raises exception, x does not gets initialized  
#print(f"x is {integers}")        