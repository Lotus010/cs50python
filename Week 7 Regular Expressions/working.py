# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 19:32:02 2022

@author: psen
"""

import re

hour1 = 0 
minute1 = 0
meridian1 = "" 
hour2 = 0 
minute2 = 0
meridian2 = "" 

def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        if not "to" in s:
            raise ValueError("ValueError")
    except ValueError:
        raise ValueError("ValueError")
        
    time = re.search(r"^([0-9]?[0-9]):?([0-9][0-9])?\ ([A-Z][A-Z])\ to\ ([0-9]?[0-9]):?([0-9][0-9])?\ ([A-Z][A-Z])$", s.strip(), re.IGNORECASE)

    hour1 = int(time.group(1))
    minute1 = int(time.group(2))
    meridian1 = time.group(3)

    hour2 = int(time.group(4))
    minute2 = int(time.group(5))
    meridian2 = time.group(6)
    
    if  minute1 >= 60 or minute2 >= 60 :
        try:
            raise ValueError("ValueError")
        except ValueError:
           raise ValueError("ValueError")
           
    if not 0 < hour1 <= 12 or not 0 < hour2 <= 12 :
        try:
            raise ValueError("ValueError")  
        except ValueError:
           raise ValueError("ValueError") 

    if meridian1 == "PM" and hour1 != "12":
        hr1 = hour1 + 12
        m1 = minute1
    else:
        hr1 =  hour1
        m1 = minute1
        
    if meridian2 == "PM" and hour2 != "12":
        hr2 = hour2 + 12
        m2 = minute2
    else:    
        hr2 = hour2
        m2 = minute2
        
        
        
        
    return f"{hr1:02d}:{m1:02d} to {hr2:02d}:{m2:02d}"





if __name__ == "__main__":
    main()