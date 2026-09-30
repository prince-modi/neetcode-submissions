class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p_s = sorted(list(zip(position, speed)))
        time = [(target - i) / j for i, j in p_s]
        # we figure out the distance each car has to go based on the position
        # and speed
        stack = []
        # using this speed in a monotonically __ stack we are basically saying the 
        # faster cars in the fleet are limited by this slowest car in the fleet
        for t in time:
        # lower means there is a faster car behind but it is not stuck in a fleet
            while stack and stack[-1] <= t:
                stack.pop()
            stack.append(t)
        return len(stack)
