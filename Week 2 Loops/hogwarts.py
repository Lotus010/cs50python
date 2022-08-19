# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 16:10:30 2022

@author: psen
"""
#Dictionary
'''
Students = {"Hermoine":"Griffyndor",
            "Draco":"Slytherin"}

for student in Students:
    print(student,Students[student],sep=",")
'''    
    
students_m = [
    {"name":"Hermoine","house":"Griffyndor","patronus":"Otter"},
    {"name":"Draco","house":"Slytherin","patronus":None},
    {"name":"Harry","house":"Griffyndor","patronus":"Stag"}  
    ]    

for s in students_m:
    print(s["name"],s["house"], sep=", ")