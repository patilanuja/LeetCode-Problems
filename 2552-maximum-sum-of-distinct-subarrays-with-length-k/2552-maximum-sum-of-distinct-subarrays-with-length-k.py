class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        n = len(nums)
        freq = {}
        max_sum = 0
        sub_sum = 0

        for ele in range(k):

            if nums[ele] in freq:
                freq[nums[ele]] += 1
            else:
                freq[nums[ele]] = 1

            sub_sum += nums[ele] 

        if len(freq) ==  k:
            max_sum = sub_sum

        for ele in range(k, n):
            sub_sum -= nums[ele-k]

            if freq[nums[ele-k]] == 1:
                freq.pop(nums[ele-k])
            else:
                freq[nums[ele-k]] -= 1

            sub_sum += nums[ele]

            if nums[ele] in freq:
                freq[nums[ele]] += 1
            else:
                freq[nums[ele]] = 1

            if len(freq) == k:
                max_sum = max(max_sum, sub_sum)

        return max_sum
            