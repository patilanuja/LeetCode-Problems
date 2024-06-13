class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = ['a','e','i','o','u']
        n = len(s)
        max_sum = 0
        sub_sum = 0

        for i in range(k):
            if s[i] in vowels:
                sub_sum += 1

        max_sum = sub_sum

        for i in range(k, n):
            if s[i-k] in vowels:
                sub_sum -= 1
            
            if s[i] in vowels:
                sub_sum += 1

            max_sum = max(max_sum, sub_sum)

        return max_sum