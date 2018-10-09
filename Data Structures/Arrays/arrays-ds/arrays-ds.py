#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverse_list0(input_list:list):
    reversed_list = []
    input_list_len = len(input_list)
    for i in range(input_list_len-1, -1, -1):
        reversed_list.append(input_list[i])
    return reversed_list


def reverse_list1(input_list:list):
    reversed_list = input_list[::-1]
    return reversed_list


def reverse_list2(input_list:list):
    reversed_list = reversed(input_list)
    return reversed_list


def reverseArray(arr:list):
    return reverse_list1(arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()