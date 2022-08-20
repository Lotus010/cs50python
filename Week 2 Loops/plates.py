# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 23:23:19 2022

@author: psen
"""

def main():
    plate = input("Plate: ").upper()
    
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
    if not 2<= len(s) <=  6:
        return False
    #No periods, spaces, or punctuation marks are allowed
    elif not s.isalnum():
        return False
    #All vanity plates must start with at least two letters
    elif not s[:2].isalpha():        
        return False          
    else:
        s = s[2:]        
        for c in s:
            if c.isalpha():                
                continue
            elif c.isnumeric():
                if c == '0':
                    return False
                elif s.isnumeric():
                    return True
                else:
                    return False
        return True
    
        
        
if __name__ == "__main__":
    main()