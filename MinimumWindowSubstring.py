################################################# Sliding Window ##########################################################
########## Time Complexity: O(n + m) ########## Space Complexity: O(m) #########

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s) or len(t) == 0:
            return ""

        map = defaultdict(int)

        for i in t:
            map[i] += 1

        left, right, minStart, charLeft, minLen = 0, 0, 0, len(t), float('inf')

        # Until we reach the end of the string
        while right < len(s):
            eChar = s[right]

            ## search till all of the chars from t string are not found
            if eChar in map :
                count = map[eChar]
                if count > 0:
                    charLeft -= 1
                map[eChar] = count - 1
            right += 1

            ## Once we have string with all characters from t
            while charLeft == 0:
                ## if substring is less than existing minimum length
                if minLen > (right - left):
                    minLen = right - left
                    minStart = left

                ## decrease window from left till you have all characters are present in the substring
                sChar = s[left]
                if sChar in map:
                    count = map[sChar]
                    if count == 0:
                        charLeft += 1
                    map[sChar] = count + 1
                left += 1
        
        return "" if minLen == float('inf') else s[minStart : minStart + minLen]