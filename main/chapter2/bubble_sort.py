# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     bubble_sort
   Description :
   Author :       zhangjian
   date：          2019/1/10
-------------------------------------------------
   Change Activity:
                   2019/1/10: 创建文件
-------------------------------------------------
"""


def bubble_sort_base(arr):

    for i in range(len(arr)-1):

        for j in reversed(range(i+1, len(arr))):
            if arr[j]<arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                is_swap = True

    return arr


def bubble_sort_opt(arr):

    # use this flag to check if array is sorted already
    is_swap = False

    for i in range(len(arr)-1):
        for j in reversed(range(i+1, len(arr))):
            if arr[j]<arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                is_swap = True
        # after each inner loop, check if the inner loop did any swap
        # if yes, reset is_swap flag to False again
        # if not, means that the arr is sorted and then return to save time for best cases
        if not is_swap:
            return arr
        else:
            is_swap = False

    return arr


def bubble_sort_main(arr):
    # bubble_sort_base(arr)
    return bubble_sort_opt(arr)