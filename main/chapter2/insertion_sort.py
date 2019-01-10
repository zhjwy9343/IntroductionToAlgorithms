# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     insertion_sort
   Description :   插入排序的Python实现
   Author :       zhangjian
   date：          2019/1/3
-------------------------------------------------
   Change Activity:
                   2019/1/3: 创建文件
-------------------------------------------------
"""


def insertion_sort(arr):
    """
    教材上数组的下标是从1开始的，因此这里对while的条件从大于0，改成了大于等于0
    :param arr:
    :return:
    """
    # 由于插入排序需要至少2个元素，所以这里需要对特殊情况进行处理
    if len(arr)<=1:
        return arr

    # 正常情况
    for j in range(1, len(arr)):
        key = arr[j]
        i = j-1
        # 这里的关键是把前一位的数字往后挪，直到前一位小于当前的key
        while (i>=0 and arr[i]>key):
            arr[i+1] = arr[i]
            i-=1
        arr[i+1] = key

    return arr


def main():
    arr = [5,2,4,6,1,3]
    print('Before sort the array is ' + str(arr))
    insertion_sort(arr)
    print('='*20)
    print('After sort the array is ' + str(arr))


if __name__ == '__main__':
    main()