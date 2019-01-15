# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     max_subarray
   Description :
   Author :       zhangjian
   date：          2019/1/15
-------------------------------------------------
   Change Activity:
                   2019/1/15: 创建文件
-------------------------------------------------
"""


def find_max_crossing_subarray(arr, low, mid, high):

    left_sum = float('-inf')
    temp_sum = 0
    for i in reversed(range(low, mid+1)):
        temp_sum += arr[i]
        if temp_sum > left_sum:
            left_sum = temp_sum
            max_left = i

    right_sum = float('-inf')
    temp_sum = 0
    for j in range(mid+1, high+1):
        temp_sum += arr[j]
        if temp_sum > right_sum:
            right_sum = temp_sum
            max_right = j

    return max_left, max_right, (left_sum + right_sum)


def find_max_subarray(arr, low, high):

    if low == high:
        return low, high, arr[low]

    mid = int((low + high) / 2)

    left_low, left_high, left_sum = find_max_subarray(arr, low, mid)
    right_low, right_high, right_sum = find_max_subarray(arr, mid+1, high)
    cross_low, cross_high, cross_sum = find_max_crossing_subarray(arr, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum


def max_subarray_main(arr):
    return find_max_subarray(arr, 0, len(arr)-1)