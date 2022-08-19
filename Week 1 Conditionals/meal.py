# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 17:15:45 2022

@author: psen
"""

def main():
    time = input("What time is it? ").split(":")
    a = convert(time)
    if 7.0 <= a <= 8.0:
        print("breakfast time")
    elif 12.0 <= a <= 13.0:
        print("lunch time")
    elif 18.0 <= a <= 19.0:
        print("dinner time")
    else:
        pass
        

def convert(time):
    hour = float(time[0])
    minute = float(time[1])/60
    return hour+minute


if __name__ == "__main__":
    main()