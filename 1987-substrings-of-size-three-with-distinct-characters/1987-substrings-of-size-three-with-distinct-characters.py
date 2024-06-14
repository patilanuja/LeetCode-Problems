class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        n = len(s)

        if n < 3:
            return 0

        good_substring = 0
        freq = {}

        for i in range(3):
            if s[i] in freq:
                freq[s[i]] += 1
            else:
                freq[s[i]] = 1

        if len(freq) == 3:
            good_substring = 1

        for i in range(3, n):

            if freq[s[i-3]] == 1:
                freq.pop(s[i-3])
            else:
                freq[s[i-3]] -= 1

            if s[i] in freq:
                freq[s[i]] += 1
            else:
                freq[s[i]] = 1 

            if len(freq) == 3:
                good_substring += 1


        return good_substring