# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Q2-4
   Description :
   Author :       zhangjian
   date：          2019/1/11
-------------------------------------------------
   Change Activity:
                   2019/1/11: 创建文件
-------------------------------------------------

这是《算法导论》(第三版)第二章的问题2-4，逆序对问题。

基本思想是使用Merge_Sort的算法，取得nlgn的时间复杂度

"""


def merge(arr, p, q, r):

    left = arr[p: q + 1]
    right = arr[q + 1: r + 1]

    left.append(float('inf'))
    right.append(float('inf'))

    i, j = 0, 0
    invs = 0
    count = False

    for k in range(p, r+1):

        if left[i] < right[j]:
            if count:
                arr[k] = left[i]
                i += 1
                invs += j
            else:
                arr[k] = left[i]
                i += 1
        else:
            arr[k] = right[j]
            j += 1
            count = True

    return invs


def inversions(arr, p, r):

    invs = 0

    if p >= r:
        return 0

    q = int((p+r)/2)

    invs += inversions(arr, p, q)
    invs += inversions(arr, q+1, r)

    invs += merge(arr, p, q, r)

    return invs


def q2_4_d(arr):

    n = len(arr)

    if n <= 1:
        return None

    return inversions(arr, 0, n-1)


def main():
    arr1 = [2, 3, 8, 6, 1]
    arr2 = [5, 4, 3, 2, 1, 0]
    arr3 = [0, 5, 4, 3, 2, 1]

    print('Inversion pairs in arr1 is %d' %q2_4_d(arr1))
    print('Inversion pairs in arr2 is %d' %q2_4_d(arr2))
    print('Inversion pairs in arr3 is %d' %q2_4_d(arr3))

    print(arr1)
    print(arr2)
    print(arr3)


if __name__ == '__main__':
    main()