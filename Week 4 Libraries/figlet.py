# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 19:23:48 2022

@author: psen
"""

import random 
import sys
from pyfiglet import Figlet

figlet = Figlet()

fontset = figlet.getFonts()

if sys.argv[1] == "-f" or sys.argv[1] == "--font":
    x = sys.argv[2]
   
    try:
        fontset.index(x)
        figlet.setFont(font=x)
    except ValueError:
        sys.exit('Invalid usage')
        
elif len(sys.argv) < 2:
    y = random.choice(fontset)
    figlet.setFont(font=y)        
else:
    sys.exit('Invalid usage')  


s = input("Input: ")

print(figlet.renderText(s))    
         