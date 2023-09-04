# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


################################################# Two Pointer Approach ##########################################################

########## Time Complexity: O(n+m) ########## Space Complexity: O(1) ##########
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy

        while list1 and list2:
            if list1.val < list2.val:
                res.next = list1
                list1 = list1.next
            else:
                res.next = list2
                list2 = list2.next
            res = res.next

        res.next = list1 or list2
        return dummy.next






        
