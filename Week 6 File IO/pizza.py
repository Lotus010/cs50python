# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 11:44:18 2022

@author: psen
"""
import csv
import sys
from tabulate import tabulate
table =[]

#Check for number of arguments and type of file
if len(sys.argv) < 2:
    sys.exit("Too few command-line argument")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line argument")
elif not sys.argv[1].endswith('.csv'):
    sys.exit("Not a CSV file")
else:
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                table.append(row)
            print(tabulate(table,headers="firstrow",tablefmt='grid'))          
    except(FileNotFoundError):
        sys.exit("File does not exist")
                  