class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_len, left, right = 0, 0, 0
        charSet = set()

        while right < len(s):
            # remove left till right ptr val in charSet
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1

            charSet.add(s[right])
            max_len = max(max_len, len(charSet))
            right += 1

        return max_len
