# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 22:47:31 2022

@author: psen
"""

def vowel(c):
    c = c.lower()
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        c = ''
    return c

def main():
    #Prompt input
    tweet = input("Enter your text: ")
    for t in tweet:
        x= vowel(t)
        print(x,end = "")
        
if __name__ == "__main__":
    main()
               