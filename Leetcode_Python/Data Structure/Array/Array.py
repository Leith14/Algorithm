# -*- coding: utf-8 -*-
# @Time    : 2021/8/26 23:54
# @Author  : Leith14
# @Email   : leixuewen14@126.com

class ArrayTest:
    def test(self):
        # create an array
        a = []

        # add element
        # Time Complexity: O(1)
        a.append(1)
        a.append(2)
        a.append(3)
        # [1, 2, 3]
        print(a)

        # Insert element
        # Time Complexity: O(N)
        a.insert(2, 99)
        # [1, 2, 99, 3]
        print(a)

        # Access element
        # Time Complexity: O(1)
        temp = a[2]
        # 99
        print(temp)

        # Update element
        # Time Complexity: O(1)
        a[2] = 88
        print(a)

        # Remove element
        # Time complexity: O(N)
        a.remove(88)
        # [1, 2, 3]
        print(a)
        a.pop(1)
        # [1,3]
        print(a)
        # Time complexity:O(1)
        a.pop()
        print(a)

        a = [1, 2, 3]

        # Get array size
        size = len(a)
        print(size)

        # Iterate array
        # Time complexity:O(N)
        # i is element not index , By careful it!!!
        for i in a:
            print(i)
        for index, element in enumerate(a):
            print("Index at", index, "is :", element)
        # i is index not element, By careful it!!!
        for i in range(0, len(a)):
            print('i:', i, "element:", a[i])

        # Find a elemnet
        # Time complexity: O(N)
        index = a.index(2)
        # 1
        print(index)

        # Sort an array
        # Time complexity: O(NlogN)
        a = [3, 1, 2]
        a.sort()
        print(a)
        # From big to small
        a.sort(reverse=True)
        print(a)


if __name__ == '__main__':
    test = ArrayTest()
    test.test()
