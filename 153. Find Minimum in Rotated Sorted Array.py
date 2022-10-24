class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 1. Initialize pointers
        l, r = 0, len(nums) - 1
        # 2. Provide default result value
        res = nums[0]
        
        # Since array is rotated such that it can result in two distinct sets of increasing numbers, 
        # where left set is always bigger than right set (unless no rotation/ rotation goes one full circle)
        # push middle-pointer to the right set where possible, unless alr established to be in the right set, 
        # then keep left to find min in that set
        while l <= r:
            # This case is where rotation = 0 or goes full circle, so min is always leftmost
            if nums[l] < nums[r]:
                return min(nums[l], res)
            m = (l + r) // 2
            # Another check
            res = min(nums[m], res)
            # if nums[m] >= nums[l] means deffo in left set, so push left-pointer to the right, else push right pointer to left
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res