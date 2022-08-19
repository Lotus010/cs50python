# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 15:20:22 2022

@author: psen
"""
def main():
    n=getnumber()
    meow(n)

#Prompt user to get number
def getnumber():
    while True:
        n = int(input("what's n? "))
        if n >0:
            break
    return n

#Print the number of meows
def meow(x):
    for _ in range(x):
        print("meow")

if __name__ == "__main__":
    main()
        