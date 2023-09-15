################################################# Sliding Window ##########################################################
########## Time Complexity: O(n) ########## Space Complexity: O(m) #########

class Solution:
    def characterReplacement(self, s: str, k: int) -> int: 

        count = {}
        res = 0
        left = 0

        for right in range(len(s)):
            # adds one to the value retrived from the count
            count[s[right]] = 1 + count.get(s[right], 0)

            if ( right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
            
        return res