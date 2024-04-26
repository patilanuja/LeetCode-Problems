class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ""
        max_len = 0

        def expand(left, right, s):
            nonlocal res, max_len

            while left >= 0 and right < len(s) and s[left] == s[right]:

                # calculate current length of substring
                current_len = right - left + 1

                # if current_len > max_len update res and max_len
                if current_len > max_len:
                    res = s[left:right+1]
                    max_len = current_len

                # expand substring 
                left -= 1
                right += 1


        for i in range(len(s)):

            # for odd len
            left, right = i, i
            expand(left,right,s)

            # for even len
            left, right = i, i+1
            expand(left, right, s)

        return res
        

        