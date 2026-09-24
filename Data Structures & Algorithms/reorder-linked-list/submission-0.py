# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        1. find mid
        2. reverse 2nd half
        3. merge two lists
        """

        #finding mid
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # mid = slow
        # reversing list from next node
        second = slow.next
        prev = slow.next = None # ending first list at slow by marking its next as None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        # here prev holds the last node which is now first node of reversed tree
        #merging two lists togethere
        first = head
        second = prev
        while first and second:
            t1 = first.next
            t2 = second.next
            first.next = second
            second.next = t1
            first = t1
            second = t2