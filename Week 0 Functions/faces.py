# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 09:39:40 2022

@author: psen
"""

#Ask user input for emoticons
def main():
    emote = input("Enter your statement emoticon ")
    convert(emote)

#Replace with emojis in convert function
def convert(s):
    t=s.replace(":)","🙂").replace(":(","🙁")
    #t=s.replace(":(","🙁")
    print(t)

#Call main function    
main()    

