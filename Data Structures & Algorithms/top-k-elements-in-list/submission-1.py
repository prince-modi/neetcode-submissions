class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap_c = [(-v,k) for k,v in Counter(nums).items()]
        heapq.heapify(heap_c)
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap_c)[1])
        return ans
        