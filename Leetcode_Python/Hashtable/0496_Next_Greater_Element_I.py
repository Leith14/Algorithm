#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 0496_Next_Greater_Element_I.py
# @Author: Xuewen Lei
# @Date  : 2021/9/15
# @Desc  :
from typing import List


class Solution:
    '''
    M is the size of nums1, N is the size of nums2
    Time Complexity: O()
    '''
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s, res, dic = [], [], {}
        for num in nums2:
            while len(s) != 0 and num > s[-1]:
                temp = s.pop()
                dic[temp] = num
            s.append(num)
        while len(s) != 0:
            dic[s.pop()] = -1

        for num in nums1:
            res.append(dic[num])

        return res
