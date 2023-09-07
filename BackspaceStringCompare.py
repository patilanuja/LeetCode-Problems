########## Time Complexity: O(m+n) ########## Space Complexity: O(1) ##########

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sptr, tptr = len(s) - 1, len(t) - 1
        scntr, tcntr = 0, 0

        while (sptr >= 0 or tptr >= 0):
            while (sptr >= 0 and (s[sptr] == '#' or scntr > 0)):
                if s[sptr] == "#":
                    scntr += 1
                else:
                    scntr -= 1
                sptr -= 1

            while (tptr >= 0 and (t[tptr] == '#' or tcntr > 0)):
                if t[tptr] == '#':
                    tcntr += 1
                else:
                    tcntr -= 1
                tptr -= 1

            if (sptr >= 0 and tptr >= 0 and s[sptr] == t[tptr]):
                sptr -= 1
                tptr -= 1
            else:
                return sptr == -1 and tptr == -1

        return True