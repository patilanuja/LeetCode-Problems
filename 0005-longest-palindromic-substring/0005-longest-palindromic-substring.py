class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longest_substring = ""
        max_len = 0

        def expand(left, right, s):

            nonlocal longest_substring, max_len

            while left >= 0  and right < len(s) and s[left] == s[right]:

                current_len = right - left + 1

                if current_len > max_len:
                     longest_substring = s[left:right+1]
                     max_len = current_len

                left -= 1
                right += 1



        for i in range(len(s)):
            
            # for even length 
            left, right = i,i
            expand(left, right,s)

            left, right = i, i+1
            expand(left, right, s)

        return longest_substring