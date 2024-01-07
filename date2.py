# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 14:08:04 2023

@author: Q418639
"""

from datetime import datetime
import pandas as pd

now = datetime.now()
print (now)
#tag = datetime(now[0:4], 8,23)
tag = datetime (now.year, now.month, now.day, 10,0,17)
print (tag)

mein_df = pd.DataFrame([[1,2,3,4,5],
                      [2,2,2,2,2],
                      [3,3,3,3,9]],
                      index = ['A','B','C'],
                      columns = [2012,2013,2014,2015,2016])

print (mein_df)
