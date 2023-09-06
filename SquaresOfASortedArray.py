################################################# Two Pointer Approach ##########################################################
########## Time Complexity: O(n) ########## Space Complexity: O(n) ##########

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left , right = 0 , n-1
        res = [None] * n
        for i in range(n-1,-1,-1):
            left_sqr = nums[left]**2
            right_sqr = nums[right]**2
            if abs(nums[left]) >= abs(nums[right]):
                res[i] = left_sqr
                left+=1
            else:
                res[i] = right_sqr
                right-=1
        return res
    
################################################# Using Sort ##########################################################
########## Time Complexity: O(nlogn) ########## Space Complexity: O(1) ##########
    class Solution:
        def sortedSquares(self, nums: List[int]) -> List[int]:
            for i in range(0,len(nums)):
                nums[i] = nums[i]*nums[i]
            nums.sort()
            return nums