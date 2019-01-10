# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     merge_sort
   Description :  实现归并排序
   Author :       zhangjian
   date：          2019/1/3
-------------------------------------------------
   Change Activity:
                   2019/1/3: 创建文件
-------------------------------------------------
"""


def merge_var1(arr, p, q, r):
    """
    Variance version one for merge. No sentinels at the end of left and right arrays, instead
    based on just the length of left and right array
    :param arr:
    :param p:
    :param q:
    :param r:
    :return:
    """
    left = arr[p: q+1]
    right = arr[q+1: r+1]

    i, j = 0, 0

    for k in range(p, r+1):
        if i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
        else:
            if i == len(left):
                arr[k] = right[j]
                j += 1
            else:
                arr[k] = left[i]
                i += 1


def merge(arr, p, q, r):
    """
    对一个输入的数组，按照p-q是一个排好序的子组，q+1到r是另外一个排好序的子组，合并这两组
    :param arr:
    :param p:
    :param q:
    :param r:
    :return:
    """
    left = arr[p: q+1]
    right = arr[q+1: r+1]

    left.append(float('inf'))
    right.append(float('inf'))

    i, j = 0, 0

    for k in range(p, r+1):
        if left[i]<=right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1


def merge_sort(arr, p, r):
    """

    :param arr:
    :param p:
    :param r:
    :return:
    """
    if p<r:
        # get split point
        q = int((p+r)/2)

        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)

        merge_var1(arr, p, q, r)

    return arr


def merge_sort_main(arr):
    n = len(arr)

    if n<=1:
        return arr

    return merge_sort(arr, 0, n-1)


def main():
    mg_tc = [0,0,0,0,0,0,0,0,2,4,5,7,1,2,3,6, 9, 9, 9, 9]
    # print(merge(mg_tc, 8, 11, 15))
    ms_tc = [0,2,4,5,7,1,8,3,6,9]
    merge_sort_main(ms_tc)
    print(ms_tc)

if __name__ == '__main__':
    main()