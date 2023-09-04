
################################################# Brute Force Approach ##########################################################
########## Time Complexity: O(n^2) ########## Space Complexity: O(1) ##########
# class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     res = []
    #     for left in range(len(nums)):
    #         right = left + 1
    #         while( right < len(nums)):
    #             if nums[left] + nums[right] == target:
    #                 res.append(left)
    #                 res.append(right)
    #             right += 1
    #     return res

class Solution:
################################################# Hash Table Approach ##########################################################
########## Time Complexity: O(n) ########## Space Complexity: O(n) ##########
                    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       mapped = {}
       for i in range(len(nums)):
           diff = target - nums[i]
           if diff in mapped:
               return [i, mapped[diff]]
           else:
               mapped[nums[i]] = i