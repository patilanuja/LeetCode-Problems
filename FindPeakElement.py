################################################# Binary Search ##########################################################
########## Time Complexity: O(log(n)) ########## Space Complexity: O(1) ##########
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        

        left, right = 1, len(nums) - 2

        if len(nums) == 1:
            return 0

        if nums[0] > nums[1]:
            return 0

        if nums[len(nums) - 1] > nums[len(nums) - 2]:
            return len(nums) - 1


        while left <= right:

            mid = (left + right) // 2

            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1] :
                return mid

            elif nums[mid] < nums[mid + 1]  :
                left = mid + 1
            
            else:
                right = mid - 1

        return -1