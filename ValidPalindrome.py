class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == '':
            return True
            
        normal_string="".join(ch for ch in s if ch.isalnum())
        input = normal_string.lower()
        output = input[::-1]

        if input == output:
            return True
        else:
            return False