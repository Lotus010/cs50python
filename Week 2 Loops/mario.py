# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 16:37:50 2022

@author: psen
"""
#size = int(input("enter the size of column: "))

#print("#\n" * size, end="")
'''
for _ in range(size):
    for _ in range(size):
        print("#", end="")
    print()   
    '''
    
def main():
    size = int(input("enter the size of column: "))
    print_square(size)

def print_square(size):
    for _ in range(size):
        print_row(size)
        
def print_row(size):
    print("#" * size)
        
if __name__ == "__main__":
    main()        



