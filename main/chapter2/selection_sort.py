# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     selection_sort
   Description :
   Author :       zhangjian
   date：          2019/1/6
-------------------------------------------------
   Change Activity:
                   2019/1/6: 创建文件
-------------------------------------------------
"""


def find_min(arr, i, s):
    # TODO: check if i and s are out of index of array
    # TODO: check if i<=s

    min_num = arr[i]
    min_idx = i
    for j in range(i, s+1):
        if arr[j]<min_num:
            min_idx = j
            min_num = arr[j]

    return min_idx


def selection_sort(arr):

    for i in range(len(arr)-1):
        min_idx = find_min(arr, i, len(arr)-1)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def main():
    arr = [0,2,4,5,7,1,8,3,6,9]
    selection_sort(arr)
    print(arr)


if __name__ == '__main__':
    main()