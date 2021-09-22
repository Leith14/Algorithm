#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 0496_Next_Greater_Element_I.py
# @Author: Xuewen Lei
# @Date  : 2021/9/7
# @Desc  :
from typing import List


class Solution:
    def nextGreaterElement(self, findNums: List[int], nums: List[int]) -> List[int]:
        st, d, ans = [], {}, []
        for v in nums:
            while st and st[-1] < v:
                d[st.pop()] = v
            st.append(v)
        for x in findNums:
            ans.append(d.get(x, -1))
        return ans
