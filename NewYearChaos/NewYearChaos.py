#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    brib = 0
    for count,num in enumerate(q,1): 
        if num - count > 0:
            if num - count >2:
                return "Too chaotic"
            brib += num - count
        elif num - count < 0 and count != len(q):
            if q[count] < num:
                brib += 1

    return brib
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
