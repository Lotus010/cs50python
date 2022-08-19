# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 13:22:33 2022

@author: psen
"""

#Prompt for response to user
response = input("Answer to Great Question of Life, the Universe and Everything ").lower()


#Check the response 
'''
if response == '42' or response == 'forty-two' or  response == 'forty two':
    print("Yes")
else:
    print("No")
'''
match response: #noqa
    case "42":
        print("Yes")
    case "forty-two":
        print("Yes")
    case "forty two":
        print("Yes")
    case _:
        print("No")