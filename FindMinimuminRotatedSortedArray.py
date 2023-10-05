#################################################  Binary Search ##########################################################
########## Time Complexity: O(logn) ########## Space Complexity: O(1) #########

class Solution:
    def findMin(self, nums: List[int]) -> int:

        left, right = 0, len(nums) - 1

        small = nums[0]

        while left <= right:

            mid = (left + right) // 2

            if nums[left] > nums[mid]:
                small = min(small, nums[mid])
                right = mid - 1

            else:
                left = mid + 1
                if (left<len(nums)):
                    small = min(small, nums[left])

        return small
        