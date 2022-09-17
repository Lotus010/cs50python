# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 15:45:13 2022

@author: psen
"""

import re



def main():
    print(count(input("Text: ")))


def count(s):
    str_list = s.strip().split()

    c = 0 

    for strs in str_list:
        if re.search(r"^um\.*", strs, re.IGNORECASE ):
            c += 1
        else:
            continue 
    
    return c        





if __name__ == "__main__":
    main()