#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    brib = 0
    for count,num in enumerate(q): 
        if num - count - 1 > 2:
            return "Too chaotic"
        for i in range(max(num-2,0),count):
            if q[count] > num:
                brib += 1
    return brib
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
