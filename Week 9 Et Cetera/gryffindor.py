# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 13:37:46 2022

@author: psen
"""

students = [{"name":"Hermonine","house":"Gryffindor"},
            {"name":"Harry","house":"Gryffindor"},
            {"name":"Ron","house":"Gryffindor"},
            {"name":"Draco","house":"Slytherin"}]

''' #List Comprehension
gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors):
    print(gryffindor)
'''
    
def is_gryf(s):
    return s["house"] == "Gryffindor"

#gryffindors = filter(is_gryf, students)   

gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)  
 
for gryffindor in sorted(gryffindors, key = lambda s: s['name']):
    print(gryffindor["name"])