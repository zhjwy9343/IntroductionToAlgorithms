# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     chapter2
   Description :
   Author :       zhangjian
   date：          2019/1/8
-------------------------------------------------
   Change Activity:
                   2019/1/8: 创建文件
-------------------------------------------------
"""

import unittest
from main.chapter4.max_subarray import max_subarray_main

# TODO: add more test cases for edge cases
max_subarray_test_case1 = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
max_subarray_test_case2 = [1, 2, 4, 5, 7, 10, 8, 3, 6, 9]


class Chapter4Test(unittest.TestCase):

    # TODO: use for loop to test all cases, rather than one by one here
    def test_max_subarray(self):
        self.assertTupleEqual (max_subarray_main(max_subarray_test_case1), (7, 10, 43), 'Correct')
        self.assertTupleEqual(max_subarray_main(max_subarray_test_case2), (0, 9, sum(max_subarray_test_case2)), 'Correct')

