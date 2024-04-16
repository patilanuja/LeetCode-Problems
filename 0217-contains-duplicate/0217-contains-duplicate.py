class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # TC: O(n) 
        # SC: O(n)
        
        # ele_to_occ = {}

        # for n in nums:
        #     if n in ele_to_occ:
        #         return True
        #     else:
        #         ele_to_occ[n] = 1
        # return False

        updated_nums = set(nums)
        
        return False if len(nums) == len(updated_nums) else True