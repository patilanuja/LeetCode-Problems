
################################################# Two Pointer Approach ##########################################################
########## Time Complexity: O(2n) ########## Space Complexity: O(1) ##########

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head

        curr = head
        cnt = 1

        while curr.next != None:
            cnt += 1
            curr = curr.next

        n = n % cnt

        t1 = t2 = head

        while( t2.next != None):
            t2 = t2.next
            if n < 1:
                t1 = t1.next
            n -= 1

        t2.next = head
        head = t1.next
        t1.next = None
        
        return head