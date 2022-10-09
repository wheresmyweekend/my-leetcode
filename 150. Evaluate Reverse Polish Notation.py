class Solution:
    def evalRPN(tokens: list[str]) -> int:
        # 1. Create stack to hold values to be operated on
        stack = []

        # 2a. if number, push to stack
        # 2b. if operator, apply operation to previous two numbers in stack (Note order for substraction adn division)
        for char in tokens:
            if char == "+":
                stack.append(stack.pop() + stack.pop())
            elif char == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
            elif char == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(char))

        # Return the last appended char, ie the answer
        return stack[0]

# Testcase
if __name__ == "__main__":
    print(Solution.evalRPN(["2","1","+","3","*"]))