class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counter = Counter(nums)
        count_vec = [[] for _ in range(len(nums) + 1)]
        ans = []
        for key, v in nums_counter.items():
            count_vec[v].append(key)
        for i in range(len(count_vec) - 1, -1, -1):
            if count_vec[i]:
                for element in count_vec[i]:
                    if len(ans) < k:
                        ans.append(element)
                    else:
                        return ans
        return ans
