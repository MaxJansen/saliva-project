# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 17:30:28 2021

@author: Max Jansen
"""

import requests

url = "https://www.rcsb.org/structure/3AQG"
r = requests.get(url)

status = r.status_code

print("Response Status: {}".format(status))
print("HTML Content:")
print(r.text)