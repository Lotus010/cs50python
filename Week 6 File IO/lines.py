# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 18:12:45 2022

@author: psen
"""

import sys

#Initialize variable to take count
c = 0

#Check for number of arguments and type of file
if len(sys.argv) < 2:
    sys.exit("Too few command-line argument")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line argument")
elif not sys.argv[1].endswith('.py'):
    sys.exit("Not a Python file")
else:
    try:
        with open(sys.argv[1]) as file:
            for line in file:
              if line.strip().startswith('#'):
                  continue
              elif len(line.strip()) == 0:
                  continue
              else:
                  c+=1
            print(c)      
    except(FileNotFoundError):
        sys.exit("File does not exist")
                  
    
    
