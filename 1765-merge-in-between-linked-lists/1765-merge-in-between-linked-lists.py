# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        dummy = ListNode(0)
        dummy.next = list1
        
        prev_a = dummy
        for _ in range(a):
            prev_a = prev_a.next

        curr_b = prev_a
        for _ in range(b-a+1):
            curr_b = curr_b.next

        list2_tail = list2
        while list2_tail.next:
            list2_tail = list2_tail.next

        list2_tail.next = curr_b.next

        prev_a.next = list2 

        return dummy.next
