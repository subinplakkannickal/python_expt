#!/bin/python3

#Link: https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
import math
import os
import random
import re
import sys

def hourglassSum(arr):
    """ Fing max of sum list of watchglasses.
    """
    return max([sum([arr_slice[colomn+1] if index==1 else sum(arr_slice[colomn : colomn+3]) \
        for index,arr_slice in enumerate(arr[row : row+3])]) \
        for row in range(4) for colomn in range(4)])
    

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)