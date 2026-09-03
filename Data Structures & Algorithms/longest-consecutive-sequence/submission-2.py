class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        final = 0
        check_set = set(nums)
        for num in check_set:
            if num - 1 in check_set:
                continue
            temp = num
            while temp in check_set:
                ans += 1
                temp += 1
            final = max(ans, final)
            ans = 0
        return final
