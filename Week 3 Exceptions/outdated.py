# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 20:00:43 2022

@author: psen
"""

month =[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

#9/8/1636
#September 8, 1636
#1636-09-08
cal = []
while True:
    try:
        date = input("Date: ")
        if len(date)<= 9:            
            cal = date.split("/")
            if int(cal[0]) > 12 or int(cal[1])>31:               
                continue
            else:
                print(f"{cal[2]}-{int(cal[0]):02}-{int(cal[1]):02}")
                break
        else:            
            cal = date.split(" ")            
            m=month.index(cal[0])
            d=cal[1].strip(',')            
            if int(d)>31:                
                continue
            else:                                              
                m = month.index(cal[0])+1 
                print(f"{cal[2]}-{m:02}-{int(d):02}")
                break
            #print("end")
    except ValueError:
        None
        

    
    


