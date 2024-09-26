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

def timeConversion(s: str) -> str:
    """Converts time in a 12-hour AM/PM format to 24-hour format.
    
    Parameters
    ----------
    s: string
        Represent a time in 12-hour clock format
    """
    
    time_flag = s[-2:]
    s = s[:-2]

    hour = int(s[:2])
    s = s[2:]

    if hour == 12:
        if time_flag == 'AM':
            new_hour = 00
        else:
            new_hour = 12
    else:
        if time_flag == 'AM':
            new_hour = hour
        else:
            new_hour = hour + 12

    full_hour = str(new_hour).zfill(2) + s
    
    return full_hour

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
