# -*- coding: utf-8 -*-
# @Time    : 2021/9/9 23:36
# @Author  : Leith14
# @Email   : leixuewen14@gmail.com


class Test:
    def test(self):
        # create hashtable by array
        hashTable = [""]*4
        # create hashtable by dictionary
        mapping = {}

        # add element
        # Time complexity:O(1)
        hashTable[1] = 'hanmeimei'
        hashTable[2] = 'lihua'
        hashTable[3] = 'siyangyuan'
        mapping[1] = 'hanmeimei'
        mapping[2] = 'lihua'
        mapping[3] = 'siyangyuan'

        # update element
        # time complexity: O(1)
        hashTable[1] = 'bishi'
        mapping[1] = 'bishi'

        # remove element
        # time complexity:O(1)
        hashTable[1] = ""
        mapping.pop(1)
        # del mapping[1]

        # get value
        # time complexity: O(1)
        var = hashTable[3]
        var1 = mapping[2]

        # check key
        # time complexity:O(1)
        # hashTable No
        3 in mapping

        # length
        len(mapping)


        # is Empty
        # time complexity:O(1)
        len(mapping) == 0


