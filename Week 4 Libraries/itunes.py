# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 14:30:02 2022

@author: psen
"""

import json 
import sys
import requests

if len(sys.argv)!= 2:
    sys.exit()
    
response = requests.get("" + sys.argv[1])    

o = response.json()

for result in o["results"]:
    print(result["trackName"])