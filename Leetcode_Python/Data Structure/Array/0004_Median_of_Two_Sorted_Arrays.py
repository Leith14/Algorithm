# -*- coding: utf-8 -*-
# @Time    : 2021/8/15 22:54
# @Author  : Leith14
# @Email   : leixuewen14@126.com
from typing import List


class Median():

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.kth(nums1, nums2, l // 2)
        else:
            return self.kth(nums1, nums2, l // 2) + self.kth(nums1, nums2, l // 2 - 1) / 2

    def kth(self, a, b, k):
        # 判断a是否为None。在python中 None,  False, 空字符串"", 0, 空列表[], 空字典{}, 空元组()都相当于False
        if not a: return b[k]
        if not b: return a[k]
        ia, ib = len(a) // 2, len(b) // 2
        ma,mb = a[ia],b[id]
        # TODO 听懂了，代码没看懂，明天继续！！！








