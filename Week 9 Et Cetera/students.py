# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 13:21:47 2022

@author: psen

Using SET
"""
students = [{"name":"Hermoine", "house":"Gryffindor"},
            {"name":"Ron","house":"Gryffindor"},
            {"name":"Harry","house":"Gryffindor"},
            {"name":"Draco","house":"Slytherin"},
            {"name":"Padma","house":"Ravenclaw"}]

'''
houses = list()  #house = []

for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])
        
for house in sorted(houses):
    print(house)        
'''
houses = set()

for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)    