#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 0020_Valid_Parentheses.py
# @Author: Xuewen Lei
# @Date  : 2021/9/3
# @Desc  :
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        stack = []
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    temp = stack.pop()
                    if c == ")":
                        if temp != "(":
                            return False
                    elif c == "]":
                        if temp != "[":
                            return False
                    elif c == "}":
                        if temp != "{":
                            return False
        return True if len(stack) == 0 else False
