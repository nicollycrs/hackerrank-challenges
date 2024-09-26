#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr, n):
    """Calculates the ratios of the elements of an array that are positive, negative, and zero.
    
    Parameters
    ----------
    arr: INTEGER_ARRAY
        An array of integers
    
    n: int
        The size of the array
    """
    # Declares counters for each case to be checked.
    zeros_count = 0
    positive_count = 0
    negative_count = 0
    
    # Verifies if the numbers are zero, positive, or negative, and increments the respective counter for each category.
    for num in arr:
        if num == 0:
            zeros_count += 1
        elif num >= 1:
            positive_count +=1
        else:
            negative_count +=1
            
    # Declares the proportion of each category.
    positive_ratio = positive_count/n
    negative_ratio = negative_count/n
    zeros_ratio = zeros_count/n
    
    # For better code readability, declaring variables for printing using a for loop.
    vars_ratio = [positive_ratio, negative_ratio, zeros_ratio]
    
    for var in vars_ratio:
        print(f"{var:.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr, n)
