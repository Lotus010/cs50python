# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 14:10:05 2022

@author: psen
"""

students = ["Hermoine","Harry","Ron"]


#Dictinoary Comprehension
gryffindor = {student:"Gryffindor" for student in students}

print(gryffindor)


#List Comprehension
gryf = [{"name":student,"house":"Gryffindor"} for student in students]

print(gryf)