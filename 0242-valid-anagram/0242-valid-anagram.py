import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        countS = collections.Counter(s)
        countT = collections.Counter(t)

        for key in countS:
            if key not in countT or countS[key] != countT[key]:
                return False

        return True