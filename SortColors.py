################################################# Two Pointer Approach ##########################################################
########## Time Complexity: O(n) ########## Space Complexity: O(1) ##########

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, curr, right  = 0, 0, len(nums) - 1

        while (curr <= right):

            if nums[curr] == 0:
                nums[curr], nums[left] = nums[left], nums[curr]
                left += 1
                curr +=1
                

            elif nums[curr] == 2:
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1

            else:
                curr += 1


