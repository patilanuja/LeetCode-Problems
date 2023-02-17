class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ## Approach 1 (Time Complexity:O(n), Space Complexity: O(1))
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low
 
        ##Approach 2 (Time Complexity:O(n), Space Complexity: O(1))
        """nums.append(target)
        nums= sorted(nums)
        return nums.index(target)"""