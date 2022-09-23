# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 16:26:53 2022

@author: psen

#########################
##    Inheritance     ##
########################
"""

class Wizard:
    def __init__(self,name):
        if not name:
            raise ValueError("Missing Name")
        self.name = name
    
class Student(Wizard):
    def __init__(self,name,house):
        super().__init__(name)
        self.house = house            


class Professor(Wizard):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject

student = Student("Harry","Gryffindor")
professor = Professor("Severus","Wizard againt Dark Arts")

         