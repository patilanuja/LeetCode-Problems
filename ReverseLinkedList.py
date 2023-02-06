# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head

        # Init pointers
        prev = head
        curr = head.next

        while curr:
            temp = curr.next # save next
            curr.next = prev # reverse node
            prev = curr # advance prev
            curr = temp # advance curr

        # prevent cycle in the ListNode
        head.next = None
        
        return prev


