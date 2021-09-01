# -*- coding: utf-8 -*-
# @Time    : 2021/8/31 21:32
# @Author  : Leith14
# @Email   : leixuewen14@gmail.com
from collections import deque


class Test:
    def test(self):
        # create linkedlist
        linkedlist = deque()

        # add element
        # time complexity:O(1)
        linkedlist.append(1)
        linkedlist.append(2)
        linkedlist.append(3)
        print(linkedlist)

        # insert element time complexity:O(N)
        linkedlist.insert(2, 99)
        print(linkedlist)

        # Access element
        # time complexity:O(N)
        element = linkedlist[2]
        # 99
        print(element)

        # search element
        index = linkedlist.index(99)
        # 2
        print(index)

        # update element
        # time complexity: O(N)
        linkedlist[2] = 88
        print(linkedlist)

        # remove element
        # time complexity O(N)
        # del linkedlist[2]
        linkedlist.remove(88)
        print(linkedlist)

        # length
        # time complexity:O(1)
        lenth = len(linkedlist)
        print(lenth)


if __name__ == '__main__':
    test = Test()
    test.test()
