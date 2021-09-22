# -*- coding: utf-8 -*-
# @Time    : 2021/9/13 22:36
# @Author  : Leith14
# @Email   : leixuewen14@gmail.com


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(t) == 0: return ''
        dic = {}
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1
        for ch in t:
            if dic.get(ch, 0) == 0:
                return ch
            else:
                dic[ch] -= 1
