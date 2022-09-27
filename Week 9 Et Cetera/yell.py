# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 12:42:16 2022

@author: psen

MAP
"""
def main():
    yell("this","is","cs50")
    
'''    
def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper().strip())
    print(*uppercased)
    
        
def yellmap(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)
'''   

def yell(words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)
    
if __name__ == "__main__":
    main()    