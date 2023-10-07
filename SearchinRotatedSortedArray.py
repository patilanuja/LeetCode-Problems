#################################################  Binary Search ##########################################################
########## Time Complexity: O(logn) ########## Space Complexity: O(1) #########

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]: # middle value is in left sorted portion
                if target > nums[mid] or target < nums[left]: # target is in right unsorted portion
                    left = mid + 1
                else:
                    right = mid - 1

            else: # middle value is in right sorted portion
                if target < nums[mid] or target > nums[right]: # target is in left unsorted portion
                    right = mid - 1
                else:
                    left  = mid + 1
                    
        return -1
        
