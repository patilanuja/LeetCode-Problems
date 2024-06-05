# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        before = ListNode(0)
        after = ListNode(0)

        beforePtr = before
        afterPtr = after

        while head:

            if head.val < x:
                beforePtr.next = head
                beforePtr  = beforePtr.next

            else:
                afterPtr.next = head
                afterPtr = afterPtr.next

            head = head.next

        afterPtr.next = None
        beforePtr.next = after.next

        return before.next