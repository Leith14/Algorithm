#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 0217_Contains_Duplicate.py
# @Author: Xuewen Lei
# @Date  : 2021/9/13
# @Desc  :
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0: return False
        s = set()
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                return True
        return False
