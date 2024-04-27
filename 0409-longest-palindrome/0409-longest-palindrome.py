import collections

class Solution:
    def longestPalindrome(self, s: str) -> int:

        res = 0
        letter_count = collections.Counter(s)

        for key in letter_count:
            if letter_count[key] % 2 == 0:
                res += letter_count[key]
            else:
                res += (letter_count[key] // 2) * 2

        if res == len(s):
            return res
        
        return res + 1
        
        