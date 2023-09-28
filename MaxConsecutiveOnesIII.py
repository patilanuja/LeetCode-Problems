################################################# Sliding Window ##########################################################
########## Time Complexity: O(n) ########## Space Complexity: O(1) #########

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        cntr0 = left = result = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                cntr0 += 1
            
            while cntr0 > k:
                if nums[left] == 0:
                    cntr0 -= 1
                left += 1
            
            result = max(result, right - left + 1)

        return result
            
            


        