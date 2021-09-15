#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 0217_Contains_Duplicate.py
# @Author: Xuewen Lei
# @Date  : 2021/9/15
# @Desc  :
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # time complexity:O(N)
        # space complexity:O(N)
        if nums is None or len(nums) == 0: return False
        s = set()
        for num in nums:
            s.add(num)
        return False if len(nums) == len(s) else True
