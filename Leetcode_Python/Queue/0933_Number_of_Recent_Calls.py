#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 0933_Number_of_Recent_Calls.py
# @Author: Xuewen Lei
# @Date  : 2021/9/2
# @Desc  :
from collections import deque


class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while len(self.q)>0 and t- self.q[0] > 3000:
            self.q.popleft()
        return len(self.q)

