class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        p_s = sorted(list(zip(position, speed)))
        time = [(target - i) / j for i, j in p_s]
        stack = []
        for t in time:
            while stack and stack[-1]<=t:
                stack.pop()
            stack.append(t)
        return len(stack)
