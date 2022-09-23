# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 15:38:39 2022

@author: psen
"""

class Student:
    def __init__(self,name,house,patronus=None):      
        self.name = name
        self.house = house
        #self.patronus = patronus
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    '''
    def charm(self):
        match self.patronus:  #NOQA
            case "Stag":
                return "🦄"
            case _:
                return "🪄"
            '''
    #Getter
    @property
    def name(self):
        return self._name
    
    #Setter
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name    

            
    #Getter
    @property
    def house(self):
        return self._house

    #Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Slytherin", "Hufflepuff"]:
            raise ValueError("Invalid House")
        self._house = house     
        
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House:")
        return cls(name,house)

def main():
    S = Student.get()
    print(S)
    



if __name__  ==  "__main__":
    main()
    
    