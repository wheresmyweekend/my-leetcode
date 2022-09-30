class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1. Assign pointers only
        l, r = 0, len(numbers) - 1

        # 2. Check target against the sum of the 2 numbers added
        # The 2 numbers are where the pointers are 
        # if sum is smaller than target, move left-pointer right 
        # else if sum is larger than target, move right-pointer left
        # else if sum is same as target, return 1-indexed values of pointers
        while l < r:
            sum = numbers[l] + numbers[r]

            if sum < target:
                l += 1
            
            elif sum > target:
                r -= 1
            
            else:
                return [l+1, r+1]
