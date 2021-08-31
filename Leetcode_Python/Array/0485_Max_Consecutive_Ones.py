# -*- coding: utf-8 -*-
# @Time    : 2021/8/28 9:57
# @Author  : Leith14
# @Email   : leixuewen14@gmail.com

'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
'''
from itertools import groupby
from typing import List


class MaxConsecutiveOnes:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        '''
        First, create a dictionary, key is iterate times of 1, value is consecutive times
        var times use to record consecutive times
        Time1 didn't finish by myself in 10minutes, so watch the solution directly!
        :param nums:
        :return:
        '''
        # d = {}
        # iterate_times = 0
        # consecutive_times = 0
        # for i in nums:
        #     if nums[i]==1:
        #         consecutive_times=consecutive_times+1
        #     else:
        #         iterate_times=iterate_times+1
        # return 0

        '''
        Solution1: iterate
        Time complexity:O(N)
        Space complexity:O(1)
        '''
        # if nums is None or len(nums) == 0:
        #     return 0
        # count = 0
        # result = 0
        # # Be careful difference syntax: range() and nums
        # for i in range(0, len(nums)):
        #     if nums[i] == 1:
        #         count += 1
        #     else:
        #         result = max(result, count)
        #         count = 0
        # return max(result, count)
        for key, g in groupby(nums):
            print(key)
            print(g)
            print(sum(g))
        # print(keyword)
        # print(max(keyword))

        return max(sum(g) for _, g in groupby(nums))


if __name__ == '__main__':
    testcase = [1, 1, 0, 1, 1, 1]
    m = MaxConsecutiveOnes()
    m.findMaxConsecutiveOnes(testcase)
