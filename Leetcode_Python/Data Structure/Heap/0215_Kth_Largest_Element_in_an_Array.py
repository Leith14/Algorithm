#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 0215_Kth_Largest_Element_in_an_Array.py
# @Author: Xuewen Lei
# @Date  : 2021/9/17
# @Desc  :
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return heapq.nlargest(k, nums)[-1]
        # time complexity: O(NlogN)
        # space comlexity: O(N)
        heap = []
        heapq.heapify(heap)
        for num in nums:
            heapq.heappush(heap, num * -1)
        while k > 1:
            heapq.heappop(heap)
            k -= 1
        return heapq.heappop(heap) * -1
