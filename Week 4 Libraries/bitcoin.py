# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 11:23:10 2022

@author: psen
"""

import requests
import sys


if len(sys.argv)!= 2:
    sys.exit("Missing command line argument")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command line argument is not a number")    
    
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit("URL error")
    
    
o = response.json()

amount = o['bpi']['USD']['rate'].replace(",","")

total = float(amount)*n

print(f"${total:,.4f}")