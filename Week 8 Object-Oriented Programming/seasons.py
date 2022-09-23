# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 19:23:25 2022
%Y-%m-%d
@author: psen
"""

from datetime import date
from datetime import datetime
import inflect
import operator
import sys

def main():
    dob = input("Date of Birth: ")
    try:
        dob_new = datetime.strptime(dob, '%Y-%m-%d')
    except ValueError:
        sys.exit("Invalid Date")        
    today = date.today()
    dob_new = datetime.date(dob_new)
    print(dob_new)
    print(today)
    delt = operator.sub(today,dob_new)
    nums = str(delt).split()[0]
    
    p = inflect.engine()
    print(p.number_to_words(nums) + " days")
    
# =============================================================================
#     if strptime(dob, '%Y-%m-%d'):
#         print("Yes")
#     else:
#         print("No")
# =============================================================================




if __name__ == "__main__":
    main()