# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 08:59:21 2020

@author: Diana McSpadden
"""
from time import time
from datetime import datetime

print("Seconds: ", time())

print("But we want to print something friendly:")


strDate = datetime.fromtimestamp(time()).strftime("%A, %B %d, %Y %I:%M:%S")
print(type(strDate))
print(strDate)

print("Now, just print the time:")
print(datetime.fromtimestamp(time()).strftime("%I:%M:%S %p"))