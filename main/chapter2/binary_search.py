# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     binary_search
   Description :
   Author :       zhangjian
   date：          2019/1/8
-------------------------------------------------
   Change Activity:
                   2019/1/8: 创建文件
-------------------------------------------------
"""


def binary_search_main(arr, v, method='iter'):
    n = len(arr)-1

    if method == 'iter':
        return binary_search_iterative(arr, v, low=0, high=n)

    if method == 'recur':
        return binary_search_recursive(arr, v, low=0, high=n)


def binary_search_iterative(arr, v, low, high):
    while low <= high:
        mid = int((low+high)/2)
        if v == arr[mid]:
            return mid
        elif v < arr[mid]:
            high = mid-1
        else:
            low = mid+1
    return None


def binary_search_recursive(arr, v, low, high):

    if low > high:
        return None

    mid = int((low+high)/2)

    if v == arr[mid]:
        return mid
    elif v < arr[mid]:
        return binary_search_recursive(arr, v, low, mid-1)
    else:
        return binary_search_recursive(arr, v, mid+1, high)