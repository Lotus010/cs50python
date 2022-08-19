# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 21:27:44 2022

@author: psen
"""

def main():
    cc = input("Enter CamelCase String: ")
    print(getsnakecase(cc))

#print(camelcase)
def getsnakecase(camelcase):
    snakecase = ''
    for c in camelcase:    
        if c.isupper():
            s = c.lower()          
            snakecase = snakecase+"_"+s
        else:
            #snakecase = snakecase+c
            snakecase += c
    return snakecase.lstrip("_")    
        
if __name__ == "__main__":
    main() 