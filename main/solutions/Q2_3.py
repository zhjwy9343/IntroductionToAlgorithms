# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     Q2_3
   Description :
   Author :       zhangjian
   date：          2019/1/10
-------------------------------------------------
   Change Activity:
                   2019/1/10: 创建文件
-------------------------------------------------
"""
import random as rd
import timeit


def compute_polynomial_base():
    n =1000
    y = 0
    A = [rd.uniform(0,2) for _ in range(n)]
    x = 0.5
    for i in range(n):
        m = 1
        for j in range(i):
            m = m * x
        y = y + A[i] * m


def compute_polynomial_horner():
    n =1000
    y = 0
    A = [rd.uniform(0,2) for _ in range(n)]
    x = 0.5
    for i in range(n, 0):
        y = A[i] + x*y


if __name__ == '__main__':
    print(timeit.timeit(stmt='compute_polynomial_base()', setup="from __main__ import compute_polynomial_base", number=1000))

    print(timeit.timeit(stmt='compute_polynomial_horner()', setup="from __main__ import compute_polynomial_horner", number=1000))