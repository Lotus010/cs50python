# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 12:43:45 2022

@author: psen
"""

import validators


email_address = input("Enter Email Adress: ")

if validators.email(email_address):
    print("Valid")
else:
    print("Invalid")    


