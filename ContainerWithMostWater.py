################################################# Two Pointer Approach ##########################################################
########## Time Complexity: O(n) ########## Space Complexity: O(1) ##########

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = min(height) 
        
        while (left < right):

            area = (right - left) * min(height[left],height[right])
            max_area = max(area, max_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area