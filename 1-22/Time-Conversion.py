#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
     # Get hours, minutes, seconds and period (AM/PM)
    hours = int(s[:2])
    minutes = s[3:5]
    seconds = s[6:8]
    period = s[-2:]
    
    # Convert to 24-hour format
    if period == "AM":
        if hours == 12:
            hours = 0
    else:  # PM
        if hours != 12:
            hours += 12
            
    # Format and return result
    return f"{hours:02d}:{minutes}:{seconds}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
