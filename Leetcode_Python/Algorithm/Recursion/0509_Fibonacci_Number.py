#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 0509_Fibonacci_Number.py
# @Author: Xuewen Lei
# @Date  : 2021/11/3


class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        mem = {0: 0, 1: 1}
        if n not in mem:
            mem[n] = self.fib(n - 1) + self.fib(n - 2)
        return mem[n]
