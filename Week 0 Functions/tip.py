# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 10:29:53 2022

@author: psen
"""

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    e = float(d.lstrip("$"))
    f = round(e,1)
    print(f)
    return f
    


def percent_to_float(p):
    q = float(p.rstrip("%"))
    r = q/100
    print(r)
    return r


main()