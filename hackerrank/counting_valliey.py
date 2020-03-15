#!/bin/python3

import math
import os
import random
import re
import sys

def countingValleys(n, s):
    level = 0
    prev_level = 0
    valley_count = 0
    for i in s:
        delta_altitude = 1 if i == "U" else -1
        level += delta_altitude
        if level == 0 and prev_level == -1:
            valley_count += 1
            
        prev_level = level

    return valley_count


if __name__ == '__main__':
    # Link: https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

    n = int(input())

    s = input()

    result = countingValleys(n, s)
