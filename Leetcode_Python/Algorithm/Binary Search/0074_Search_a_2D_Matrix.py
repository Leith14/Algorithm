#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 0074_Search_a_2D_Matrix.py
# @Author: Xuewen Lei
# @Date  : 2021/10/29
from typing import List


class Solution:
    # solution1:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) is 0 or matrix is None:
            return False
        col, row = len(matrix[0]), len(matrix)
        left, right, level = 0, col - 1, 0
        while level < row:
            left, right = 0, col - 1
            while left <= right: # 如果不加=,这个[[1]],1,这个testcase会报错,binary search 要考虑一个元素的情况
                mid = left + (right - left) // 2
                if target == matrix[level][mid]:
                    return True
                elif target > matrix[level][mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            level += 1
        return False