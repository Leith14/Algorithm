#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 1456_Maximum_Number_of_Vowels_in_a_Substring_of_Given_Length.py
# @Author: Xuewen Lei
# @Date  : 2021/11/3


class Solution:
    # Sliding Window
    # N is the size of s
    # Time complexity: O(N)
    # Space complexity: O(1)
    def maxVowels(self, s: str, k: int) -> int:
        if s is None or len(s) is 0 or len(s) < k:
            return 0
        vowels = ("a", "e", "i", "o", "u")
        count, res, = 0, 0
        for i in range(0, k):
            if s[i] in vowels:
                count += 1
        res = max(res, count)
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                count -= 1
            if s[i] in vowels:
                count += 1
            res = max(res, count)
        return res


if __name__ == '__main__':
    sl = Solution()
    s = "abciiidef"
    k = 3
    print(sl.maxVowels(s, k))
