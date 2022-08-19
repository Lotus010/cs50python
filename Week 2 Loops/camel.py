# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 18:49:11 2022

@author: psen
"""
def main():
    cc = input("Enter CamelCase String: ")
    getsnakecase(cc)

#print(camelcase)
def getsnakecase(camelcase):
    for c in camelcase:    
        if c.isupper():
            print("_",c.lower(),end = '')        
        else:
            print(c,end = '')
                
        
if __name__ == "__main__":
    main()        
