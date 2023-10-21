################################################# Linked List ##########################################################
########## Time Complexity: O(n) ########## Space Complexity: O(1) #########



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        ## 1 -> 2 -> 3 -> 4 -> 5

        slow , fast = head, head

        # Find Middle Node
         ## 1 -> 2 -> 3 -> 4 -> 5
         ##          ^
         ##          |
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        # Reverse the second half
        ## 1 -> 2 -> 3 <- 4 <- 5
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Reorder list
        left = head
        right = prev
        
        while right.next and left.next:
            # point left node to right node
            leftNext = left.next
            left.next = right
            left = leftNext
            # point right node to left node
            rightNext = right.next
            right.next = left
            right = rightNext
