class Solution:
    def isPalindrome(x: int) -> bool:
        # Convert to string and use left and pointers and increment/decrement inwards
        x = str(x)
        l, r = 0, len(x) - 1
        while l < r:
            if x[l] == x[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
    
    def isPalindrome_v2(x: int) -> bool:
        # create a reverse version of the original number and compare it to the unaltered version 
        reverse = 0
        original = x

        while original > 0:
            reverse = reverse * 10 + original % 10
            original = original // 10
        
        return reverse == x


# Testcase
if __name__ == "__main__":
    x = 13531
    print(Solution.isPalindrome_v2(x))