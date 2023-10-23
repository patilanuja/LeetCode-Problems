################################################# Two Pointer ##########################################################
########## Time Complexity: O(n) ########## Space Complexity: O(1)  #########

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        t1 = t2 = head

        while (t2 != None):
            t2 = t2.next
            if (n < 0):
                t1 = t1.next
            n -= 1

        if (n == 0):
            head = head.next
            return head

        else:
            t1.next = t1.next.next

        return head
        