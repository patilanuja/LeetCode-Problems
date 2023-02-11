# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #By the time the second pointer reaches the end of the list, the first pointer will be at the middle node. 
        slow = fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        return slow
        

        