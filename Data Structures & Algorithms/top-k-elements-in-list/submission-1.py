from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        modified = list(counts.items())
        converted = list(map(lambda el: list(el), modified))

        # print(f"Converted: {converted}")
        
        for item in converted:
            item[0], item[1] = item[1], item[0]
        
        # print(f"Converted: {converted}")
        
        max_heap = []
        for pair in converted:
            heapq.heappush(max_heap, [-pair[0], pair[1]])
        
        retrieved = []
        for i in range(k):
            removed = heapq.heappop(max_heap)
            retrieved.append(removed[1])
        
        return retrieved
        
