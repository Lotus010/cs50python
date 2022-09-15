# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 12:55:06 2022

@author: psen
"""
import csv
import sys

table = []
#Check for number of arguments and type of file
if len(sys.argv) < 3:
    sys.exit("Too few command-line argument")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line argument")
elif not sys.argv[1].endswith('.csv') or not sys.argv[1].endswith('.csv'):
    sys.exit("Not a CSV file")
else:
    try:
        #Read data from CSV to list
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            next(reader, None)  # skip the headers
            for row in reader:
                lastname,firstname = row[0].split(',')
                table.append([firstname.strip(),lastname,row[1]])
            
        #Write data to CSV    
        with open(sys.argv[2], "a", newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["firstname","lastname","house"])
            writer.writeheader()
            for firstname,lastname,house in table:
                writer.writerow({"firstname":firstname,"lastname":lastname,"house":house})
    except(FileNotFoundError):
        print(f"Could not read {sys.argv[1]}")
        sys.exit
                  