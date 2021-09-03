#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Stack.py
# @Author: Xuewen Lei
# @Date  : 2021/9/3
# @Desc  :

class Test:
    def test(self):
        # create a stack
        stack = []

        # add element
        # time complexity:O(1)
        stack.append(1)
        stack.append(2)
        stack.append(3)
        print(stack)

        # get the top of stack
        # time complexity: O(1)
        var = stack[-1]
        print(var)

        # remove the top of stack
        # time complexity: O(1)
        temp = stack.pop()
        print(f"top element {temp}")

        # get stack length
        # time complexity:O(1)
        len(stack)
        if len(stack) == 0:
            pass

        # iterate stack
        # time complexity:O(N)
        while len(stack) > 0:
            temp = stack.pop()
            print(temp)


if __name__ == '__main__':
    test = Test()
    test.test()
