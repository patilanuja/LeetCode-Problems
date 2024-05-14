# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None and list2 is None: return None
        if list1 is None: return list2
        if list2 is None: return list1

        new = ListNode()
        dummy = new

        while list1 and list2:

            if list2.val > list1.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next

            dummy = dummy.next

            dummy.next = list1 or list2

        return new.next