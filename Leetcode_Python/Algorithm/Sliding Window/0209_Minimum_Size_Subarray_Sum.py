#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 0209_Minimum_Size_Subarray_Sum.py
# @Author: Xuewen Lei
# @Date  : 2021/11/1
from typing import List


class Solution:
    # Sliding Window / Two Pointer
    # N is the size of nums
    # Time complexity: O(N)
    # Space comlexity: O(1)
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) is 0 or nums is None:
            return 0
        i, j, total, res = 0, 0, 0, len(nums) + 1
        while j < len(nums):
            total += nums[j]
            j += 1
            while total >= target:
                res = min(res, j - i)
                total -= nums[i]
                i += 1
        return 0 if res == len(nums) + 1 else res