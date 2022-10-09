class MinStack:
    # Main idea is to have 2 stacks, 1 for regular values, 1 to track the minimum value of the stack up until that point
    # For each value pushed, the minStack checks if the new value is smaller than current minimum, and acts accordingly
    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack == []:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]

if __name__ == "__main__":
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(2)
    obj.push(0)
    obj.push(-10)
    obj.push(3)
    obj.push(3)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()
    print(param_3)
    print(param_4)