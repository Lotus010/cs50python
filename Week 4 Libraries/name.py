# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 14:12:59 2022

@author: psen
"""

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments") 


print("My name is", sys.argv[1])

    