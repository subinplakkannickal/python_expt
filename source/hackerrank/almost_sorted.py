#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the almostSorted function below.
def almostSorted(arr):
    len_of_arr = len(arr)
    if len_of_arr == 2:
        if arr[0] > arr[1]:
            print ('yes\nswap 1 2')
        else:
            print ("yes")
        return
        
    a_list = []

    for i in range(len_of_arr - 1):
        if arr[i] > arr[i + 1]:
            a_list.append(i + 1)

    # print (a_list)

    if not a_list:
        print ("yes")
    elif len(a_list) == 1:
        if arr[a_list[0] - 1] < arr[a_list[0] + 1] \
          and arr[a_list[0] - 2] < arr[a_list[0]]:
            print ('yes\nswap {} {}'.format(a_list[0] , a_list[0] +1))
            return
        print ("no")
    elif len(a_list) == 2:
        print ('yes\nswap {} {}'.format(a_list[0], a_list[1] + 1))
    else:
        for i in range(len(a_list) - 1):
            if a_list[i] > a_list[i + 1]:
                print ("no")
                return
        print ('yes\nreverse {} {}'.format(a_list[0], a_list[-1] + 1))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    print (len(arr))
    almostSorted(arr)
