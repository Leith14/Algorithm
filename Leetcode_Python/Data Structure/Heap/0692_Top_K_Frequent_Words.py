#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 0692_Top_K_Frequent_Words.py
# @Author: Xuewen Lei
# @Date  : 2021/9/18
# @Desc  :
import heapq
from typing import List


class Solution:
    # Heap + HashTable
    # N is the size of words
    # Time complexity: O(NlogK)
    # Space complexity: O(N)
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mapping = {}
        # for word in words:
        #     mapping[word] += 1
        for word in words:
            if word not in mapping:
                mapping[word] = 0
            mapping[word] += 1
        print(mapping)
        heap = []
        for key, value in mapping.items():
            heapq.heappush(heap, Node(key, value))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        while len(heap) > 0:
            temp: Node = heapq.heappop(heap)
            print(temp.key, '', temp.value)
            res.append(temp.key)

        res.reverse()
        return res


# Create a Node to include key, value
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, nxt):
        return self.key > nxt.key if self.value == nxt.value else self.value < nxt.value
