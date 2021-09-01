#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 0206_Reverse_Linked_List.py
# @Author: Xuewen Lei
# @Date  : 2021/9/1
# @Desc  :

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        while head is not None and head.next is not None:
            dummy.next = head.next

