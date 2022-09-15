# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 14:56:34 2022

@author: psen
"""

import re



def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if match := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)", ip.strip()):
        if match.group(1)<="255" and match.group(2)<="255" and match.group(3)<="255" and match.group(4)<="255"  :
            return True
        else:
            return False
    else:
        return False
    





if __name__ == "__main__":
    main()