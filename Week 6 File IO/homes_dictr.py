# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 15:23:06 2022

@author: psen
"""

import csv

students = []

with open("students_head.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]} )
        
for student in sorted(students, key = lambda student:student["name"]):
    print(f"{student['name']} is from {student['home']}")   
    