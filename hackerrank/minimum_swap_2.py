#!/bin/python3

#Link: https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
import math
import os
import random
import re
import sys

def minimumSwaps(arr):
    """ Find swap count to sort the list.
    """
    swap_count = 0
    temp = [i for _, i in sorted(zip(arr, range(len(arr))))]

    for i in   range(len(arr)):
        if arr[i] != i+1:
            swap_count += 1
            temp[arr[i] - 1] = temp[i]
            arr[i], arr[temp[i]] = i + 1, arr[i]

    return swap_count

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    print(res)

