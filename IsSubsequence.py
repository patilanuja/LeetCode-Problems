################################################# Two Pointer Approach ##########################################################
########## Time Complexity: O(max(len(s), len(t))) ########## Space Complexity: O(1) ##########

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sptr, tptr  = 0, 0

        if len(s) > len(t):
            return False

        while sptr < len(s) and tptr < len(t) :
            if s[sptr] == t[tptr] :
                sptr += 1
            tptr += 1
        return len(s) == sptr