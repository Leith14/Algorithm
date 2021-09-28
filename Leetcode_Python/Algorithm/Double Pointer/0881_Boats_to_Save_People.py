#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 0881_Boats_to_Save_People.py
# @Author: Xuewen Lei
# @Date  : 2021/9/28
# @Desc  :
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        '''
        Two pointers: N is the size of people
        time complexity:O(NlogN)
        :param people:
        :param limit:
        :return:
        '''
        if len(people) == 0 or people is None: return 0
        people.sort()
        left = 0
        right = len(people) - 1
        boats = 0
        while left <= right:
            # if left == right:
            #     boats += 1
            #     break
            # if people[left] + people[right] > limit:
            #     boats += 1
            #     right -= 1
            # else:
            #     boats += 1
            #     right -= 1
            #     left += 1
            # 饲养员解法,逻辑更简洁，学习一下
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boats += 1
        return boats
