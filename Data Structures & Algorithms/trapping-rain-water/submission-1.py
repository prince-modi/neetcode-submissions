class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        ans = 0
        while left < right:
            if height[left] <= height[right]:
                left += 1
                ans += max(min(leftMax, rightMax) - height[left], 0)
                leftMax = max(leftMax, height[left])
            else:
                right -= 1
                ans += max(min(leftMax, rightMax) - height[right], 0)
                rightMax = max(rightMax, height[right])
        return ans
