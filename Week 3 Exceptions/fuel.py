# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 20:46:20 2022

@author: psen
"""
def main():
    a = check_fuel("Enter tank reading: ")
    print_check(a)

def check_fuel(prompt):
    while True:
        try:
            fuel = input(prompt).split('/',3)        
            x = int(fuel[0])
            y = int(fuel[1])
            if x>y:
                continue
            return round((x/y)*100)        
        except (ValueError, ZeroDivisionError):
            pass    
        

def print_check(z):    
    if z <=1 :
        print("E")
    elif 100 >= z >= 99:
        print("F")
    else:
        print(f"{z}%")
     
if __name__ == "__main__":
    main()    
  