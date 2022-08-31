# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 11:08:42 2022

@author: psen
"""

import random


def main():
    le = get_level()
    generate_integer(le)


def get_level():
    while True:
        try:
            Level = int(input("Level: "))
            if Level == 1 or Level == 2 or Level == 3:
                return Level
            else:
                continue
            
        except TypeError :
            continue


def generate_integer(level):
    if level == 1:
        for _ in range(10):
            x = random.randint(1, 9)
            y = random.randint(1, 9)
            c = 1
            while True:
                a = int(input(f"{x} + {y} = "))
                if a == x+y:
                    break
                else:
                    if c ==3:
                        print(f"{x} + {y} =",x+y)
                        c = 0
                        break
                    print("EEE")
                    c += 1
                    continue
     
    if level == 2:
        for _ in range(10):
            x = random.randint(10, 99)
            y = random.randint(10, 99)
            c = 1
            while True:
                a = int(input(f"{x} + {y} = "))
                if a == x+y:
                    break
                else:
                    if c ==3:
                        print(f"{x} + {y} =",x+y)
                        c = 0
                        break
                    print("EEE")
                    c += 1
                    continue

    if level == 3:
        for _ in range(10):
            x = random.randint(100, 999)
            y = random.randint(100, 999)
            c = 1
            while True:
                a = int(input(f"{x} + {y} = "))
                if a == x+y:
                    break
                else:
                    if c ==3:
                        print(f"{x} + {y} =",x+y)
                        c = 0
                        break
                    print("EEE")
                    c += 1
                    continue                
                


if __name__ == "__main__":
    main()