class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # 1. Initialise pointers for binary search
        l,r = 0, len(nums) - 1
        
        # Since sorted array is rotated such that left set of numbers is always larger than right set (see testcase), 
        # move pointer towards set containing target
        while l <= r:
            # Defining middle-pointer
            m = (l+r) // 2
            # Checking if middle-pointer is pointing at target
            if nums[m] == target:
                return m

            # if middle-pointer inside left set of numbers
            if nums[l] <= nums[m]:
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            # if middle pointer is in right set of numbers
            else:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1

# Testcase
if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2] # flipped from [0,1,2,4,5,6,7]
    target = 0
    ans = Solution().search(nums, target);
    print(ans)
