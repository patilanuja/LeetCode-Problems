class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        max_sum = 0
        sub_sum = 0

        freq = {}

        if k > n: return 0

        for i in range(0,k):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1

            sub_sum += nums[i]

        if len(freq) == k:
            max_sum = max(max_sum, sub_sum)

        for i in range(k,n):
            
            sub_sum -= nums[i-k]

            if freq[nums[i-k]] == 1:
                freq.pop(nums[i-k])
            else:
                freq[nums[i-k]] -= 1

            sub_sum += nums[i]

            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1

            if len(freq) == k:
                max_sum = max(max_sum, sub_sum)

        return max_sum