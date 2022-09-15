# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 11:54:04 2022

@author: psen
"""

import re 

URL = "my username is https://twitter.com/preeti_chobey/status/1570118220660744192"

user = re.search(r"(?:https?://)?(?:www\.)?twitter\.com/([A-Za-z0-9_]+)", URL.strip(), re.IGNORECASE)

print(f"USERNAME: {user.group(1)}")