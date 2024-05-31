# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head

        prev_left = dummy
        # traverse till left 
        for _ in range(left - 1):
            prev_left = prev_left.next

        # reverse the list part from left to right

        start = prev_left.next
        curr = start
        prev = 0
        for _ in range(right-left+1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # connect first part to the reversed list
        prev_left.next = prev

        # connect everthing after right to the reversed part
        start.next = curr

        return dummy.next

        