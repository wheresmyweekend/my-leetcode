class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1. Initialise pointers for binary search. The pointers will check possible eating speeds from 1 banana per hour to maximum number of bananas per hour
        #    Maximum number of bananas is based on the biggest pile
        l, r = 1, max(piles)
        # Note: result is initially assigned to 'r' in case number of hours = number of piles; This case requires eating all piles in one hour each
        res = r
        
        # 2. Binary search thru possible eating speeds, and updates minimum eating speed required until the search space is completed.
        while l <= r:
            # Defining current eating speed being tested 
            k = (l + r) // 2
            # Initialising time variable 
            hours = 0
            for p in piles:
                # Note: math.ceil rounds up division
                hours += math.ceil(p / k)
            if hours <= h:
                # Updating minimum eating speed with each while-loop
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        
        return res