# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = dummyHead = ListNode(0,head)
        fast = head

        i = 0
        while fast:
            if i>=n:
                slow = slow.next
            fast = fast.next
            i+=1
        slow.next = slow.next.next if slow.next else None
        return dummyHead.next 