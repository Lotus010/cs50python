# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 15:12:48 2022

@author: psen

UNPACKING

"""

"""
def total(galleons,sickles,knuts):
    return (galleons*27 + sickles)*17 + knuts

coins = [100,50,25]

print(total(*coins), "knuts")

dict_coin = {"galleons":100,"knuts":25, "sickles":50}

print(total(**dict_coin), "knuts")
"""
def f(*args, **kwargs):
    if args:
        print("Positional:", args)
    else:
        print("Named:", kwargs)

f(100,15,25)
f(L=100,G=10)

    