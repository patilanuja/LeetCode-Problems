class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        smallest = float('inf')
        stack = []

        for curr_n in nums:

            while stack and curr_n >= stack[-1][-1]:
                stack.pop()

            if stack and curr_n > stack[-1][0]:
                return True

            stack.append((smallest, curr_n))
            smallest = min(smallest, curr_n)
        return False