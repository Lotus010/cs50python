# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 11:42:08 2022

@author: psen
"""

#Create Nutrition Table using dictionary
Fruits = {"Apple" : "130",
          "Avocado" : "50",
          "Banana" : "110",
          "Cantaloupe" : "50",
          "Grapefruit" : "60",
          "Grapes" : "90",
          "Honeydew Melon" : "50",
          "Kiwifruit" : "90",
          "Lemon" : "15",
          "Lime" : "20",
          "Nectarine" : "60",
          "Orange" : "80",
          "Peach" : "60",
          "Pear" : "100",
          "Pineapple" : "50",
          "Plums" : "70",
          "Strawberries" : "50",
          "Sweet Cherries" : "100",
          "Tangerine" : "50",
          "Watermelon" : "80"
          }

fruit = input("Enter Fruit: ")
if fruit in Fruits:
    print(Fruits[fruit])
else:
    None


