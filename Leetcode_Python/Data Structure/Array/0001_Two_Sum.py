# -*- coding: utf-8 -*-
# @Time    : 2021/8/15 18:50
# @Author  : Leith14
# @Email   : leixuewen14@126.com
from typing import List


class Solution:
    '''
    思路：循环数组，判断target-n是否在数组中？如果是输出index
    '''

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            '''
            判断target - n是否在已经遍历过的元素中
            '''
            if m in d:
                return [d[m], i]
            else:
                # 存储数组信息key：数组值，value；index
                # 遍历一个就存一个进来
                d[n] = i
