class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        ## Approach 1 (sort) (Time Complexity:O(n log n), Space Complexity: O(n))
        """num = sorted(nums)
        i = 0

        while i < len(num):
            if i+1 < len(num) and  num[i] == num[i+1]:
                return True       
            else:
                i += 1
        return False"""

        ## Approach 2 (dictionary) (Time Complexity:O(n), Space Complexity: O(n))
        """
        dictionary = {}
        for i in nums:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1

        for value in dictionary.values():
            if value >1:
                return True
        else:
            return False """


        ## Approach (set)  (Time Complexity:O(n), Space Complexity: O(n))
        return False if len(nums) == len(set(nums)) else True
        
            