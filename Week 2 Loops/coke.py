# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 21:44:58 2022

@author: psen
"""

#coin = int(input("Enter coins: "))

    
due = 50
co = 0

while True:
    #Prompt User
    print("Amount Due:",due)
    coins = int(input("Insert Coin: "))
    #Check Valid coins
    if coins == 10 or coins == 25 or coins == 5:
        coin = coins
    else:
        continue
    #Calculate Amount Due and Change owed
    due = due - coin
    co = co + coin
    #Print Change    
    if due <= 0:
        print("Change Owed:", co-50)
        break 
    else:
        print("Change Owed: 0")
        continue