#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def get_hourglass_sum(matrice_3_3:list):
    row0 = matrice_3_3[0]
    row2 = matrice_3_3[2]
    center = matrice_3_3[1][1]
    return sum(row0) + center + sum(row2)


def get_submatrice(matrice:list, row_start:int, row_end:int, column_start:int, column_end:int):
    submatrice = []
    for row_index in range(row_start, row_end):
        row = matrice[row_index][column_start:column_end]
        submatrice.append(row)

    return submatrice

def get_submatrices(matrice:list, sub_row_size:int, sub_column_size:int):
    matrice_row_size = len(matrice)
    matrice_column_size = len(matrice[0])
    submatrices = []

    for row_index in range(0, matrice_row_size-sub_row_size+1):
        for column_index in range(0, matrice_column_size-sub_column_size+1):
            submatrice = get_submatrice(matrice,
                                        row_index, row_index+sub_row_size,
                                        column_index, column_index+sub_column_size)
            submatrices.append(submatrice)

    return submatrices


def hourglassSum(arr:list):
    submatrices = get_submatrices(matrice=arr, sub_row_size=3, sub_column_size=3)

    max_sum = get_hourglass_sum(submatrices[0])
    for submatrice in submatrices:
        sum = get_hourglass_sum(submatrice)
        if sum >= max_sum:
            max_sum = sum

    return max_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()