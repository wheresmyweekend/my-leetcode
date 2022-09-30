class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # 2. Assign left & right pointers to start and end of string
        l, r = 0, len(s) - 1

        # 3. Compare char on each pointer
        while l < r:
            # 3a. Check position and if alphanumeric
            # continuously ignore non-alphanumeric until next one
            # while keeping relative pointer position valid
            while l < r and not self.check(s[l]):
                l += 1
            while r > l and not self.check(s[r]):
                r -= 1
            
            # 3b. Compare pointers 
            if s[l].lower() != s[r].lower():
                return False
            
            # 3c. Move pointers 1 step
            l += 1
            r -= 1

        return True

    
    # 1. Create function to check if char is alphanumeric
    def check(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
