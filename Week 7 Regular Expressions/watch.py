# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 19:14:22 2022

@author: psen
"""

import re



def main():
    print(parse(input("HTML: ")))


def parse(s):
    url = re.search(r"https://www\.youtube\.com/embed/(\w+)", s.strip(), re.IGNORECASE)

    return f"https://youtu.be/{url.group(1)}"


...


if __name__ == "__main__":
    main()