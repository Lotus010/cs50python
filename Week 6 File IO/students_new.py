# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 12:38:25 2022

@author: psen
"""

students = []

with open("students.csv") as file:
    for line in file:
        name,house = line.rstrip().split(",")
        #student = {}
        #student["name"] = name 
        #student["house"] = house
        student = {"name":name,"house": house}
        students.append(student)
        
def get_name(student):
    return student["name"]      

#def get_house(student):
#    return student["house"]

for student in sorted(students, key = get_name):
    print(f"{student['name']} and {student['house']}")
    
for student in sorted(students, key = lambda paramname: student["house"]):
    print(f"{student['name']} and {student['house']}")    