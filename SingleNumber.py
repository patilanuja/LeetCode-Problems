class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        ## Using Dictionary (Time complexity: O(n) , Space Complexity: O(n) )
        eleDict = {}
        for ele in nums:
            if ele in eleDict:
                eleDict[ele] += 1
            else:
                eleDict[ele] = 1

        for ele in eleDict:
            if eleDict[ele] == 1:
                return ele

        ## Using Default Dictionary (Time complexity: O(n) , Space Complexity: O(n))

        eleDict = defaultdict(int)
        for ele in nums:
            eleDict[ele] += 1

        for ele in eleDict:
            if eleDict[ele] == 1:
                return ele
        
        ## Using count (Time complexity: O(n^2), Space Complexity: O(1) )
        for ele in nums:
            if nums.count(ele) == 1:
                return ele


        ## Using Math (Time complexity: O(n), Space Complexity: O(n))
        return 2 * sum(set(nums)) - sum(nums)


        ## Using sort (Time complexity: O(n * log(n)) , Space Complexity: O(1) )
        nums.sort()
        for i in range(0, len(nums) - 1, 2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return(nums[len(nums) - 1])
    
        ## Using XOR (Time complexity: O(n) , Space Complexity: O(1) )
        final = 0
        for i in nums:
            final ^= i
        return final
    
        ## Using two pointer (Time complexity: O(nlon(n)) , Space Complexity: O(1) )
        prev = None
        nums = sorted(nums)
        for  i in range(len(nums)-1):
            curr = nums[i]
            nxt = nums[i+1]
            if curr != prev and curr < nxt:
                return curr
            prev = curr
        return nums[-1]
     





