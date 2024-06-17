class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(', ']':'[', '}':'{'}
        stack = []

        for bracket in s:
            if bracket == '(' or bracket == '[' or bracket == '{':
                stack.append(bracket)
            elif stack and brackets[bracket] == stack[-1]:
                stack.pop()
            else:
                return False
        return False if stack else True