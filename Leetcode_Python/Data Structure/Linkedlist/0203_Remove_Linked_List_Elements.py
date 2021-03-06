#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 0203_Remove_Linked_List_Elements.py
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
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        while head is not None:
            if head.val == val:
                prev.next = head.next
                head = head.next
            else:
                prev = head
                head = head.next
        return dummy.next

