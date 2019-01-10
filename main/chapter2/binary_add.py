# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     binary_add
   Description :
   Author :       zhangjian
   date：          2019/1/5
-------------------------------------------------
   Change Activity:
                   2019/1/5: 创建文件
-------------------------------------------------
"""

def binary_add(arr_a, arr_b, arr_c):
    flag = 0
    n = len(arr_a)
    for i in range(n):
        key = arr_a[i] + arr_b[i] + flag
        arr_c[i] = key % 2

        if key>1:
            flag = 1

    if flag==1:
        arr_c[n] = flag

    return arr_c


def main():
    n = 10
    arr_a = [1]*n
    arr_b = [0]*n
    arr_b[0] = 1
    arr_c = [0]*(n+1)
    print(arr_a)
    print(arr_b)
    print(binary_add(arr_a, arr_b, arr_c))


if __name__ == '__main__':
    main()