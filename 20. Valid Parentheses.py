class Solution:
    def isValid(s: str) -> bool:
        # 1a. Create hashmap to match open and closing brackets
        brackets = {")":"(", "}":"{", "]":"["}
        # 1b. Create stack to hold open brackets
        stack = []

        for char in s:
            # 2. If its an open bracket, add to stack
            if char not in brackets.keys():
                stack.append(char)
            else:
                # 3. If its a closing bracket, 
                # 3a. check if stack empty and 
                # 3b. check if last-added open bracket matches
                if stack != [] and brackets[char] in stack[-1]:
                    stack.pop()
                else:
                    return False
        # 4. if all pairs are cleared, return true
        if stack == []:
            return True
        else:
            return False
            

# Testcase
if __name__ == "__main__":
    s = "}])"
    print(Solution.isValid(s))