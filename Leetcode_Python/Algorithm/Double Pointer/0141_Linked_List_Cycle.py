# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Time complexity: O(N)
    # Space complexity: O(1)
    def hasCycle(self, head: ListNode) -> bool:
        if head is None: return False
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = head.next
            fast = head.next.next
            if slow == fast:
                return True
        return False


