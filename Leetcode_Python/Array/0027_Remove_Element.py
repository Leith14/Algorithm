# -*- coding: utf-8 -*-
# @Time    : 2021/8/31 21:25
# @Author  : Leith14
# @Email   : leixuewen14@gmail.com
from typing import List


class Solution:
    # double pointers
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums is None or len(nums) == 0:
            return 0
        l, r = 0, len(nums) - 1
        while l < r:
            while l < r and nums[l] != val:
                l += 1
            while l < r and nums[r] == val:
                r -= 1
            nums[l], nums[r] = nums[r], nums[l]
        return l if nums[l] == val else l + 1

        # solution2: index
        index = 0
        for num in nums:
            if num != val:
                nums[index] = num
                index += 1
        return index
