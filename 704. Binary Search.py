class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1. Make pointers to limit search area
        l,r = 0, len(nums) - 1

        # 2. Basically find midpoint of search area, check if target is bigger or smaller than midpoint, and shift pointers
        #    depending on whether target is bigger or smaller than number at current midpoint. return index if target = num at midpoint of course
        #    This continues until search area is 0 and then return -1
        while l <= r:
            m = (r+l) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1