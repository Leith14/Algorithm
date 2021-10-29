#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 0162_Find_Peak_Element.py
# @Author: Xuewen Lei
# @Date  : 2021/9/30
from typing import List


class Solution:
    # Binary Search
    # N is the size of nums
    # Time Complexity: O(log N)
    # Space Complexity: O(1)
    def findPeakElement(self, nums: List[int]) -> int:
        if nums is None or len(nums) is 0:
            return -1
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l
