class Solution:
    # Recursion function modifies the global variables within the main function by going thru each possible if-statement choices and 
    # goes into next recursion by modifying 'combination' variable or returning to previous layer after adding a proper 'combination' to 'combinationList'
    # Function rules:
    #   - number of open brackets must always be more or equal to number of close brakets
    #   - Can only add close brackets when number of close brakets < number of open brackets
    #   - recursion continues until all pairs are utilized
    def recursionFunction(combinationList, combination, openBracketCount, closeBracketCount, numberOfPairsRequired):
        if openBracketCount == closeBracketCount == numberOfPairsRequired:
            combinationList.append(combination)
            return 
        
        if openBracketCount < numberOfPairsRequired:
            Solution.recursionFunction(combinationList, combination + "(", openBracketCount + 1, closeBracketCount, numberOfPairsRequired)
        
        if closeBracketCount < openBracketCount:
            Solution.recursionFunction(combinationList, combination + ")", openBracketCount, closeBracketCount + 1, numberOfPairsRequired)

    def generateParenthesis(self, n: int) -> list[str]:
        # 1. Create the string combination to hold a particular valid combination of brackets
        combination = ""
        # 2. Create a list to store valid combinations
        combinationList = []
        # 3. Call the recursion function to directly modify the 'combinationList' variable
        Solution.recursionFunction(combinationList, combination, 0, 0, n)
        # 4. Return the list
        return combinationList

# Testcase
if __name__ == "__main__":
    n = 4
    print(Solution().generateParenthesis(n))

