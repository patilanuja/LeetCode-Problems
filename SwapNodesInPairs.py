################################################# Two Pointer Approach ##########################################################
########## Time Complexity: O(n) ########## Space Complexity: O(1) ##########

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:

            first = prev.next
            second = prev.next.next

            # Swapping nodes
            first.next = second.next
            second.next = first
            prev.next = second

            prev = first

        return dummy.next

            