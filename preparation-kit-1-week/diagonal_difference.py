#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr, n):
    """Calculates the absolute difference between the sums of a given square matrix's diagonals.
    
    Parameters
    ---------
    arr: list
        a matrix of integers
        
    n: int
        numbers of rows and columns in the square matrix arr
    """
    
    primary_diagonal = []

    for i in range(0, n):
        primary_diagonal.append(arr[i][i])


    c = n
    secondary_diagonal = []

    for r in range(0, n):
        c -= 1
        secondary_diagonal.append(arr[r][c])


    absolute_difference = abs((sum(primary_diagonal)) - (sum(secondary_diagonal)))
    
    return absolute_difference

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr, n)

    fptr.write(str(result) + '\n')

    fptr.close()
