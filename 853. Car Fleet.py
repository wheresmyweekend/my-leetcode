class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # zip lets you 'zip up' to seperate arrays of same length to form 1 array of arrays
        # 1. Creates a combined array for each car's initial position and speed
        pair = [[p,s] for p,s in zip(position, speed)] 
        # 2. Create a stack to hold time required to reach target distance for each vehicle
        stack = []

        # 3. Sorts the combined array. and iterates it in reverse. Firstly determines time taken to reach destination for each vehicle and appends it to the stack
        #    If stack length is 2 or more, check the last-appended time (stack[-1]) with previous appended time (stack[-2]). If last-appended time is shorter, it means it would reach
        #    destination before the car infront, and hence will form a fleet somewhere before the finishline. Because of this, the stack is popped to simulate the two cars travelling as a fleet as per question
        #    Since each subsequent possible fleet will be slower than the preceeding one, no need to check all fleets, just the most recent one. Hence, use stack
        for p,s in sorted(pair)[::-1]:
            stack.append((target - p) / s )
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)