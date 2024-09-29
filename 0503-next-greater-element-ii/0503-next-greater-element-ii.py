class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        nge = [-1]*len(nums)

        for idx, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                nge[stack.pop()] = num

            stack.append(idx)

        for idx, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                nge[stack.pop()] = num

        return nge