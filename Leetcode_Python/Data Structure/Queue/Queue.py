#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Queue.py
# @Author: Xuewen Lei
# @Date  : 2021/9/2
# @Desc  :
from collections import deque


class Test:
    def test(self):
        # create a queue
        queue = deque()

        # add element
        # time complexity O(1)
        queue.append(1)
        queue.append(2)
        queue.append(3)
        print(queue)

        # get head of the queue
        # time complexity O(1)
        temp1 = queue[0]
        print(temp1)

        # remove the head of the queue
        temp2 = queue.popleft()
        print(temp2)
        print(queue)

        # queue is empty?
        # time complexity O(1)
        if len(queue) == 0:
            pass

        # length of the queue
        len(queue)

        # iterate queue
        # time complexity O(N)
        while len(queue) != 0:
            temp = queue.popleft()
            print(temp)


if __name__ == '__main__':
    test = Test()
    test.test()
