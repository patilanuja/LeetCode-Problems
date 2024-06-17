class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        top = self.stack[-1]
        del self.stack[-1]
        return top
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        minEle =  self.stack[0]
        for i in range(len(self.stack)):
            if self.stack[i] < minEle:
                minEle = self.stack[i]
        return minEle
            
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()