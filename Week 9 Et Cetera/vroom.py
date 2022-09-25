# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 14:42:48 2022

@author: psen

Argsparse
"""

import argparse

parser = argparse.ArgumentParser(description = "Vroom the Car")
parser.add_argument("-n", default = 1, help = "number of vrooms", type = int)
args = parser.parse_args()

for _ in range(args.n):
    print("vroom")