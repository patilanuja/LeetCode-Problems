class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

         # TC = O(n) and SC = O(k)

        n = len(nums)
        sub_sum = 0
        max_sum = 0
        freq = {}

        for i in range(k):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1

            sub_sum += nums[i]

        if len(freq) == k:
            max_sum = sub_sum

        for i in range(k,n):
            sub_sum -= nums[i-k]

            if freq[nums[i-k]] == 1:
                freq.pop(nums[i-k])
            else:
                freq[nums[i-k]] -= 1


            sub_sum += nums[i]

            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1

            if len(freq) == k:
                max_sum = max(max_sum, sub_sum)

        return max_sum




        