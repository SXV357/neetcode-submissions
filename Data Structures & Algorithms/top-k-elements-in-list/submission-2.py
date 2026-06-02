from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counts = Counter(nums)
        
        buckets = [[] for _ in range(n)]
        
        for key, val in counts.items():
            buckets[val-1].append(key)
        
        modified = list(filter(lambda bucket: len(bucket) > 0, buckets))

        result = []
        flag = False

        for bucket in reversed(modified):
            for el in bucket:
                result.append(el)
                if len(result) == k:
                    flag = True
                    break
            
            if flag: break
        
        return result
                    