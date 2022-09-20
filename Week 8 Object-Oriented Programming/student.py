# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 15:38:39 2022

@author: psen
"""

class Student:
    def __init__(self,name,house):
        self.n = name
        self.h = house
    ...
    

def main():
    S = get_student()
    print(f"{S.name} from {S.house}")


def get_student():
    n = "Harry"
    h = "Gryffindor"      
    student = Student(n,h)
    return student


if __name__  ==  "__main__":
    main()
    
    