class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Step 1a: Define hashmap to store occurance of each alphabets in string
        count = {}
        # Step 1b: Initialise result, and left and right pointers
        res = 0
        l, r = 0,0

        for r in range(len(s)):
            # Step 2: Update the count hashmap with each occurance of every letter in string
            count[s[r]] = 1 + count.get(s[r], 0)
            
            # Step 3: For each substring, based on hashmap containing number of occurance of each substring, 
            # see if the amount of changes required to match the letter with highest occurance to substring length
            # to maximise window length. If number of required changes is larger than 'k', shift left point to reduce window size
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            # Step 4: Calculate max window size based on current size and overall max
            res = max(res, (r - l + 1))
        return res