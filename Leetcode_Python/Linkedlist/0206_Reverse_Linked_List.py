<<<<<<< HEAD
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 0206_Reverse_Linked_List.py
# @Author: Xuewen Lei
# @Date  : 2021/9/1
# @Desc  :
=======
# -*- coding: utf-8 -*-
# @Time    : 2021/9/1 21:49
# @Author  : Leith14
# @Email   : leixuewen14@gmail.com
>>>>>>> origin/master

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

<<<<<<< HEAD
=======

>>>>>>> origin/master
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        while head is not None and head.next is not None:
<<<<<<< HEAD
            dummy.next = head.next

=======
            dnext = dummy.next
            hnext = head.next
            dummy.next = hnext
            head.next = hnext.next
            hnext.next = dnext
        return dummy.next
>>>>>>> origin/master
