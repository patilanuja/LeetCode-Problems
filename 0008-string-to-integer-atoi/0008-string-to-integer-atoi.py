class Solution:
    def myAtoi(self, s: str) -> int:
        
        # whitespaces
        # +/- sign
        # min, max
        # number

        i = 0
        negative = 1
        res = 0
        min_int, max_int = -2**31, 2**31 - 1

        #whitespaces
        while i < len(s) and s[i] == ' ':
            i += 1

        # +/- sign
        if  i < len(s) and s[i] == '+':
            negative = 1
            i += 1
        elif i < len(s) and s[i] == '-':
            negative = -1
            i += 1

        # number
        number_list = '0123456789'
        while i < len(s) and s[i] in number_list:
            res = res * 10 + int(s[i])
            i += 1


        # +/-
        res = res * negative

        if res < min_int:
            return min_int
        elif res > max_int:
            return max_int
        else:
            return res