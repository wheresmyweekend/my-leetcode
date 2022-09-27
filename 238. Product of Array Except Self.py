class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) #creates a default array of 1's of length of input array

        # increments the prefix to result
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # increments postfix to result array backwards
        postfix = 1
        for k in range(len(nums) -1, -1, -1):
            res[k] *= postfix
            postfix *= nums[k]

        return res
