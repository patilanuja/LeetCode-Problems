class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets = {')':'(', ']':'[', '}':'{'}
        stack = []

        for ch in s:
            if ch is '(' or ch is '[' or ch is '{':
                stack.append(ch)
            else:
                if stack and brackets[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return False if len(stack) > 0 else True