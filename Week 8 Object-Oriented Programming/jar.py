# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 13:59:20 2022

@author: psen
"""

class Jar:
    
    
    def __init__(self,capacity=12):
        
        self.capacity = capacity        
        self.cookie_jar = 0
        
    def __str__(self):
        return self.cookie_jar * "0"

    def deposit(self,n):        
        if self.cookie_jar + n > self.capacity:
            raise ValueError("Too many cokkies")
        self.cookie_jar = self.cookie_jar + n 
    
    def withdraw(self,n):
        if self.cookie_jar - n < 0:
            raise ValueError("Too less cookies")
        self.cookie_jar = self.cookie_jar - n    
    
    @property
    def capacity(self):
        return self._capacity 
    
    @capacity.setter
    def capacity(self,capacity):
        if capacity < 0:
            raise ValueError("Invalid")
        self._capacity = capacity    
    
   
    
    @property
    def size(self):
        size = self.cookie_jar  
        return size
    
    
        

def main():
    j = Jar(20)
    j.deposit(6)
    j.withdraw(3)
    print(j)
    print(j.capacity)
    
    print(j.size) 
    
if __name__ == "__main__":
    main()    
    
    