# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     linear_search
   Description :
   Author :       zhangjian
   date：          2019/1/5
-------------------------------------------------
   Change Activity:
                   2019/1/5: 创建文件
-------------------------------------------------
"""


def linear_search(arr, v):

    for i in range(len(arr)):
        if arr[i] == v:
            return i

    return None


def main():
    arr = [1,2,3,4,5,6,7,8]
    v = 8
    print(linear_search(arr, v))


if __name__ == '__main__':
    main()