# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head

        newPointer = dummy

        while newPointer.next and newPointer.next.next:


            # assign pointers
            curr = newPointer.next
            adj = newPointer.next.next
            
            # Adjust links # swap
            curr.next = adj.next
            adj.next = curr

            #connect links 
            newPointer.next = adj
            newPointer = curr

        return dummy.next
