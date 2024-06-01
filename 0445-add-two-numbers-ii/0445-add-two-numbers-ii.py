# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        carry = 0
        dummy = ListNode(0)
        new = dummy

        while l1 or l2 or carry:

            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0

            sum = digit1 + digit2 + carry

            digit = sum % 10
            carry = sum //10

            new.next = ListNode(digit)
            new = new.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return self.reverse(dummy.next) 
            



    def reverse(self, head):
        curr = head 
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
        