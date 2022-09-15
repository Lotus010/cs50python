# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 10:16:25 2022

@author: psen
"""
import re

name = input("What's your name? ").strip()

if matches := re.search(r"^(.+), *(.+)$", name):
    last,first = matches.groups()
    #name = first + " " + last
    name = f"{matches.group(2)} {matches.group(1)}"
print(name)    

    