class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1. Create answer array
        answer = []

        # 2. Sort input array from smallest to largest
        nums.sort()

        # 3. Setup main loop to move 1 pointer, 
        # while dynamically updating 2 internal pointers to match target value of '0'
        # and add array of values to answer array
        for index, value in enumerate(nums):
            # 3a. Checks if current value of main loop pointer 
            # is same as previous and skip that is the case
            # to avoid duplicate answers
            if index > 0 and value == nums[index-1]:
                continue

            # 3b. Sub loop for 2 internal pointers;
            # Pointers are restricted to the rightside of main-loop pointer
            # since any value to the left of main point is iterated through for answers
            l, r = index + 1, len(nums)-1
            while l < r:
                sum = value + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    answer.append([value, nums[l], nums[r]])
                    # 3c. Increments l to check if next number is duplicate 
                    # to prevent repeat answers 
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        
        return answer
            