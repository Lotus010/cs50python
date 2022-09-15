# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 16:22:49 2022

@author: psen

. - any character except a newline
* - 0 or more repetitions
+ - 1 or more repetitions
? - 0 or 1 repetition
{m} - m repetitions
{m,n} - m–n repetitions
^ - matches the start of the string
$ - matches the end of the string or just before the newline at the end of the string
[] - set of characters
[^] - complementing the set
 \d - decimal digit
\D - not a decimal digit
\s - whitespace characters
\S - not a whitespace character
\w - word character … as well as numbers and the underscore
\W - not a word character

"""

import re

def main():
    email = "abc_police@gmail.com"
    valid_email(email)
    
'''
if "@" in email and "." in email:
    print("valid")
else:
    print("invalid")
'''

def valid_email(email_id):
    if re.match(r"^(\w|\.)+@(\w|\.)+?\w+\.(edu|org|com)$", email_id.strip(), re.IGNORECASE):
        print("Valid")
    else:
        print("Invalid")    
        
        

if __name__ == "__main__":
    main()     