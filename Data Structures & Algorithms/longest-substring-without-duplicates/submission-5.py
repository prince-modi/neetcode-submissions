class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        ans = 0

        left, right = 0, 0
        while right < len(s):
            if s[right] in check:
                while s[right] in check:
                    check.remove(s[left])
                    left += 1
            check.add(s[right])
            ans = max(ans, right - left + 1)
            right += 1

        return ans
