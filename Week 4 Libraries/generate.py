# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 13:41:12 2022

@author: psen
"""
'''
import random 

coin = random.choice(["head","tail"])


from random import choice

coin = choice(["head","tail"])

print(coin)

import random

number = random.randint(1, 10)
print(number)
'''
import random

cards = ["King","Queen","Jack","Ace"]
random.shuffle(cards)
for card in cards:
    print(card)