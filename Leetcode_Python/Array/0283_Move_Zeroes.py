# -*- coding: utf-8 -*-
# @Time    : 2021/8/31 21:20
# @Author  : Leith14
# @Email   : leixuewen14@gmail.com
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # solution1:index
        index = 0
        for num in nums:
            if num != 0:
                nums[index] = num
                index += 1
        for i in range(index, len(nums)):
            nums[i] = 0

        # solution2: double pointers
        zero = 0  # records the position of "0"
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
