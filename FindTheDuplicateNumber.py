#################################################  Two Pointer Approach ##########################################################
########## Time Complexity: O(n) ########## Space Complexity: O(1) ##########

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow, fast = 0, 0

        while True:

            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                slow = 0

                while slow != fast:
                    slow = nums[slow]
                    fast = nums[fast]

                return fast