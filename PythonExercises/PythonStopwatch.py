# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 13:57:36 2020

@author: Diana McSpadden
"""
# import needed libraries
import time as t
import numpy as np

# define timer value
t0 = 0

def clearTimer():
    t0 = 0


def stopWatch(startOrStop):
    global t0
    
    if startOrStop == "START":
        # get the start time in seconds
        t0 = t.time()
    elif startOrStop == "STOP":
        # get the difference in time
        timerSeconds = t.time() - t0;
        # clear the timer
        clearTimer()
        
        return timerSeconds

# clear t0
clearTimer()

# Now that I have the functions let's time kronecker multiplication
x = np.arange(4).reshape(2, 2)
y = np.arange(5, 9).reshape(2, 2)
print(x)
print(y)

# start the timer and run multiplication
stopWatch("START")
result = np.kron(x, y)
# stop the timer
kronSeconds = stopWatch("STOP")

print(result)
print("Kron multiplication of x and y took ", kronSeconds, " seconds.")
      
        
        
        

        
    