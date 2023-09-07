################################################# Two Pointer Approach ##########################################################
########## Time Complexity: O(n) ########## Space Complexity: O(1) ##########
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left , right = 0, 1

        while (right < len(nums)):

            if nums[left] != 0:
                left += 1
                right += 1

            elif nums[right] == 0:
                right += 1

            else:
                nums[left], nums[right] = nums[right], nums[left]