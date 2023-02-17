# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:      
        ## Time Complexity:O(n), Space Complexity: O(1)
        if not head:
            return head

        prev = curr = head

        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr = prev.next
            else:
                prev = curr
                curr = curr.next

        if head.val == val:
            return head.next
        return head