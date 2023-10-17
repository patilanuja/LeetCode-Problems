################################################# Two Pointer ##########################################################
########## Time Complexity: O(n) ########## Space Complexity: O(1) ##########

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newList = None
        current = head

        while current:
            next_node = current.next
            current.next = newList
            newList = current
            current = next_node

        return newList

