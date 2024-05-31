# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr_node = slow
        prev = None

        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = next_node

        first_half = head
        second_half = prev
        max_val = 0

        while second_half:
            max_val = max(max_val, first_half.val + second_half.val)
            first_half = first_half.next 
            second_half = second_half.next

        return max_val

        