import collections
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:


        # create s_dict and p_dict
        s_count = collections.Counter(s[:len(p)-1])
        p_count = collections.Counter(p)

        result = []
        left = 0

        # loop through the string s

        for i in range(len(p)-1, len(s)):

            # add first element from remaining string
            s_count[s[i]] += 1

            if s_count == p_count:
                result.append(left)

            s_count[s[left]] -= 1

            if s_count[left] == 0:
                del s_count[left]

            left += 1

        return result




        

        