################################################# Two Pointer ##########################################################
########## Time Complexity: O(n) ########## Space Complexity: O(1) ##########

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        fast = head 

        while fast and fast.next:
            head = head.next
            fast = fast.next.next
            if head is fast:
                return True
        return False

        