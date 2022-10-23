class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # 1. Create array with default value 0
        res = [0] * len(temperatures)
        # 2. Create stack to hold pairs of [temperature, index]
        stack = []

        # note: enumerates allow to loop thru array providing both index and value
        # 3. loops thru given array and appends stack with values until a larger value is found, after which it starts popping the stack,
        #    comparing the index difference between the larger temp and popped temp and appending it tot results array;
        #    This is done until the no larger value can be found (while-loop)
        for i,t in enumerate(temperatures):
            # while stack means 'if stack has existing values'
            # t > stack[-1][0] means 'current temp (t) from enumerate is larger than temp ([0]) from top of stack (stack[-1])'
            while stack and t > stack[-1][0]:
                # temperature and index from the stack
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])       
        return res

# Testcase
if __name__ == "__main__":
    temperatures = [73,74,75,71,69,72,76,73]
    print(Solution().dailyTemperatures(temperatures))