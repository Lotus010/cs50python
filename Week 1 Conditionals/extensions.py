# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 15:05:20 2022

@author: psen
"""


filename = input("File name: ").lower()

file = filename[-4:]


match file:             #noqa
    case ".gif":
        print("image/gif")
    case ".jpg":
        print("image/jpeg")
    case "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case ".pdf":
        print("application/pdf")
    case ".txt":
        print("application/txt")
    case ".zip":
        print("application/zip")
    case _:
        print("application/octet-stream")
   
