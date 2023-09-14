################################################# Sliding Window ##########################################################
########## Time Complexity: O(n) ########## Space Complexity: O(1) #########

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        add = 0 
        final = len(nums) + 1

        for right in range(len(nums)):
            add += nums[right]
            while add >= target:
                final = min(final, right-left + 1)
                add -= nums[left]
                left += 1

        return 0 if final == len(nums) + 1 else final