class Solution:
    def firstUniqChar(self, s: str) -> int:
        ## Approach 1 (Time Complexity:O(n), Space Complexity: O(n))
        """dictionary = {}
        for ele in s:
            if ele not in dictionary:
                dictionary[ele] = 1
            else:
                dictionary[ele] += 1

        for key,value in dictionary.items():
            if value == 1:
                return s.index(key)
        return -1 """


        ## Approach 2 (Time Complexity:O(n), Space Complexity: O(1))
        """cnt = Counter(s)
        print(cnt)
        for i,v in enumerate(s):
            if cnt[v] == 1:
                return i
        return -1"""


        ## Approach 3 (Time Complexity:O(n^2), Space Complexity: O(1))
        for i in range(len(s)):
            if s[i] not in s[0:i] and s[i] not in s[i+1:]:
                return i
        return -1