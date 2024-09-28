#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    """Finds the minimum and maximum values that can be calculated by summing exactly four of the five integers of an array.
    
    Parameters
    ----------
    arr: list
        An array of 5 integers.
    """

    # Creates a list to save sum results.
    miniMaxSumArr = []

    # Iterates the array summing every element, except for the current index.
    for i, _ in enumerate(arr):
        aux = arr.copy()
        aux.pop(i)
        miniMaxSumArr.append(sum(aux))
        
    # Gets the min and maximum values from the sum results.
    minVal = min(miniMaxSumArr)
    maxVal = max(miniMaxSumArr)

    # Prints the results
    print(f"{str(minVal)} {str(maxVal)}")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
