# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 14:37:49 2022

@author: psen
"""

from random import choice

class TV:
    channels = ["Netflix","Hotstar","Prime","TV Plus"]
    
       
    @classmethod
    def get(cls):
        return choice(cls.channels)
        
        
def main():
    print(TV.get())

if __name__ == "__main__":
    main()

       
    