#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Set.py
# @Author: Xuewen Lei
# @Date  : 2021/9/15
# @Desc  :


class Test:
    def test(self):
        # create a Set
        s = set()

        # add element
        s.add(10)
        s.add(3)
        s.add(5)
        s.add(2)
        s.add(2)
        # {2, 10, 3, 5}
        print(s)

        # Search element
        # time complexity: O(1)
        print(2 in s)

        # delete element
        # time complexity:O(1)
        s.remove(2)
        # {10, 3, 5}
        print(s)

        # length
        len(s)


if __name__ == '__main__':
    test = Test()
    test.test()
