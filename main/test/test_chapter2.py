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
from main.chapter2.merge_sort import merge_sort_main
from main.chapter2.insertion_sort import insertion_sort
from main.chapter2.binary_search import binary_search_main


# TODO: add more test cases for edge cases
sort_test_case1 = [5,2,4,6,1,3]
sort_test_case2 = [0,2,4,5,7,1,8,3,6,9]

binary_search_test_case1 = [2,3,11,34,456,567,868,6654,78654,678986]


class Chapter2Test(unittest.TestCase):

    # TODO: use for loop to test all cases, rather than one by one here
    def test_merge_sort(self):
        self.assertListEqual(merge_sort_main(sort_test_case1), [1,2,3,4,5,6], 'Correct')
        self.assertListEqual(merge_sort_main(sort_test_case2), [0,1,2,3,4,5,6,7,8,9], 'Wront')


    def test_insertion_sort(self):
        self.assertListEqual(insertion_sort(sort_test_case1), [1,2,3,4,5,6], 'Correct')
        self.assertListEqual(insertion_sort(sort_test_case2), [0,1,2,3,4,5,6,7,8,9], 'Wront')


    def test_binary_search(self):
        self.assertEqual(binary_search_main(binary_search_test_case1, 6654), 7)
        self.assertEqual(binary_search_main(binary_search_test_case1, 555), None)


    def test_binary_search(self):
        self.assertEqual(binary_search_main(binary_search_test_case1, 6654, method='recur'), 7)
        self.assertEqual(binary_search_main(binary_search_test_case1, 555, method='recur'), None)
