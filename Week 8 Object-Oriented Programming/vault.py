# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 17:36:45 2022

@author: psen

###############################
##  Operator Overloading    ##   
#############################

"""

class Vault:
    def __init__(self,Galleon,Sickle,Knut):
        self.Galleon = Galleon
        self.Sickle = Sickle
        self.Knut = Knut
     
    def __str__(self):
        return f"{self.Galleon} Galleon, {self.Sickle} Sickle, {self.Knut} Knut"
        
    def __add__(self,other):
        Galleon = self.Galleon + other.Galleon
        Sickle = self.Sickle + other.Sickle
        Knut = self.Knut + other.Knut
        return Vault(Galleon,Sickle,Knut)
    
Harry = Vault(100,75,50)
Ron = Vault(50,75,100)
print(Harry + Ron)

        





