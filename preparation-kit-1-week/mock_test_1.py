#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def findMedian(arr: list):
 """Finds the median of a give list of numbers.
 Parameters
 ----------
 arr: list
   An array of integers.
 Returns
 -------
 median
   The median of the list.
 """
 arr.sort()
 is_Odd = True if len(arr) % 2 != 0 else False
 n = len(arr)
  
 if is_Odd:
   i = int((n-1)/2)
   median = arr[i]
 else:
   i = int(n/2)
   median = (arr[i] + arr[i-1])/2

 return median

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
