class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 1. Create hashset to store substring
        charSet = set()
        
        # 2. Create back pointer and result integer
        l = 0
        res = 0
        
        # 3. Create sliding window by continuously adding letters to hashset
        # until the pointer hits the 2nd occurance of an existing letter in hashset
        # while-loop will finally activate, removing all letters starting from 
        # the left of the main string until first occurance of the offending letter is removed.
        # The letter at the front pointer is then added, then substring length calculated,
        # and sliding window continues.
        for r in range(len(s)):
            # The removal of chars from left up till duplicate
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            # Continuous adding of char until duplicate occurs
            charSet.add(s[r])
            # Calculation of substring length
            res = max(res, r - l + 1)
        return res
