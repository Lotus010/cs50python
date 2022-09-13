# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 11:55:43 2022

@author: psen
"""

import csv

students = []

with open("students_home.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})

for student in sorted(students, key = lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")