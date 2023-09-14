################################################# Sliding Window ##########################################################
########## Time Complexity: O(n) ########## Space Complexity: O(m) where m= size of the charset #########


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        charset = set()

        left, max_len = 0,0

        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left += 1
            charset.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len