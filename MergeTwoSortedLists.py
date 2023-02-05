# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        ## if list1 is Null append list2
        if list1 is None:
            return list2

        ## if list2 is Null append list1
        if list2 is None:
            return list1
            
   
        ## Initialization of temp node
        ## 1st temp node is the head of the new merged node
        
        if list1.val < list2.val:
            temp = newHead = ListNode (list1.val)
            list1 = list1.next

        else:
            temp = newHead = ListNode(list2.val)
            list2 = list2.next

        while(list1 is not None or list2 is not None):


            ## Append list2 if list1 becomes none
            if list1 is None:
                temp.next = ListNode(list2.val)
                list2 = list2.next
            ## Append list1 if list2 becomes none
            elif list2 is None:
                temp.next = ListNode(list1.val)
                list1 = list1.next

            ## if both lists are not none, check for the lowest value from list1 and list2 and append it to temp
            else:
                if list1.val < list2.val:
                    temp.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    temp.next = ListNode(list2.val)
                    list2 = list2.next

            temp = temp.next
        return newHead






        
