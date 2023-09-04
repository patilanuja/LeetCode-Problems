################################################# Two Pointer Approach ##########################################################

########## Time Complexity: O(n) ########## Space Complexity: O(1) ##########

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       left, right = 0, len(numbers) - 1
       
       while (left < right):
            add = numbers[left] + numbers[right]
            if add < target:
                left += 1
            elif add > target:
                right -= 1
            else:
                return [left+1, right+1]
            