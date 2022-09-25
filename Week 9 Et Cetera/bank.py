# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 13:44:23 2022

@author: psen

global
"""

class Account:
    def __init__(self):
        
        self._balance = 0
        
    @property
    def balance(self):
        return self._balance

    def deposit(self,n):
        self._balance += n
        return self._balance
    
    def withdraw(self,n):
        self._balance -= n
        return self._balance
    
def main():
    account  = Account()
    print("Balance: ", account.balance)
    account.deposit(100)
    account.withdraw(30)
    print("Balance: ", account.balance)
    
if __name__ == "__main__":
    main()
        