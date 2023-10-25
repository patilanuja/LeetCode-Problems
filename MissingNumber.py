########## Time Complexity: O(n2) ########## Space Complexity: O(1) ##########
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return False
        
        for i in range(0, len(nums)+1):
            if i not in nums:
                return i