class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 1. Define pointers and result
        l, r, res = 0, len(height) - 1, 0

        # 2. Shift pointers accordingly to determine largest area (result),
        # starting from the extremes. Pointers are shifted if they are the smaller of the 
        # two pointers as there is potential to make the smaller pointer larger by shifting.
        # result is updated if new area is larger than previous area. 
        while l < r:
            res = max(res, (r-l) * min(height[l], height[r]))
            if height[l] <= height[r]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
        return res