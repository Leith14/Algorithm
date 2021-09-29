#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 0035_Search_Insert_Position.py
# @Author: Xuewen Lei
# @Date  : 2021/9/29
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # time complexity: O(logN)
        # space complexity: O(1)
        # TODO 其实还有点不是很清楚right和left赋值为什么不一样，再多看几遍
        if nums is None or len(nums) is 0:
            return 0
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left
