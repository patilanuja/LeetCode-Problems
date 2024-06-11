class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_water = 0

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            max_water = max(max_water, (h*w))

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_water