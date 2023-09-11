################################################# Sliding Window ##########################################################
########## Time Complexity: O(n) ########## Space Complexity: O(1) ##########

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, max_add, curr = 0, sum(nums[:k]), sum(nums[:k])
        for right in range(k, len(nums)):
            curr += nums[right]

            if (right - left + 1) > k:
                curr -= nums[left]
                left += 1

            max_add = max(curr, max_add)

        return max_add / k

