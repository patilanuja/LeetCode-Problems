class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        left = cntr = result = 0

        for right in range(len(nums)):
           
            if nums[right] == 0:
               cntr += 1

            while cntr > 1: 
                if nums[left] == 0:
                    cntr -= 1
                left += 1
                        
            result = max(result, right - left)

        return result
