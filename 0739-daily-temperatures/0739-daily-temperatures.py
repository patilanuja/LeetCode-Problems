class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        l = len(temperatures)
        result = [0]*l

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                result[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)

        return result
