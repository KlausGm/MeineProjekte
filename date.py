# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 14:08:04 2023

@author: Q418639
"""

from datetime import datetime

now = datetime.now()
print (now)
#tag = datetime(now[0:4], 8,23)
tag = datetime (now.year, now.month, now.day, 10,0,17)
print (tag)
print (now.timestamp())