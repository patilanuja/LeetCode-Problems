class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.size = 0
        self.stack = []
        

    def push(self, x: int) -> None:
        if self.size < self.maxSize:
            self.stack.append(x)
            self.size += 1
            # print(self.stack)


    def pop(self) -> int:
        if self.size > 0:
            top = self.stack[-1]
            del self.stack[-1]
            self.size -= 1
            # print(top)
            return top
        else:
            return -1
        

    def increment(self, k: int, val: int) -> None:
        j = min(k, self.size)

        for i in range(j):
            self.stack[i] += val
        

        


        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)