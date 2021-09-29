#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 0704_Binary_Search.py
# @Author: Xuewen Lei
# @Date  : 2021/9/28
# @Desc  :
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0 or nums is None: return -1
        l = 0
        r = len(nums) - 1
        while l <= r:  # 如果不加=,这个[5],这个testcase会报错
            # l + (r - l)为了不超出整数边界，因为直接l+r/2,l+r有可能会超出int范围
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return -1
