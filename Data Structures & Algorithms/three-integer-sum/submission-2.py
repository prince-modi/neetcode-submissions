class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = set()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            target = -nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                t2 = nums[j] + nums[k]
                if t2 > target:
                    k -= 1
                    # while j <= k and nums[k - 1] == nums[k]:
                    #     k -= 1
                elif t2 < target:
                    j += 1
                elif nums[i] + nums[j] + nums[k] == 0:
                    ans.add(tuple([nums[i], nums[j], nums[k]]))
                    j += 1
                    k -= 1
                    # break
        return [i for i in ans]
