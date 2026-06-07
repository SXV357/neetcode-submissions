# revisiting this one since couldn't come up with truly optimal solution 1st time

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        naive approach

        count frequencies of all elements
        since we want most frequent ones we sort the items in descending order by
        frequency then simply extract the first k keys since they correspond to the k
        most frequent elements

        let n = len(nums)

        overall complexity ~ O(n log n) since it dominates
        '''

        # O(n)
        freq = Counter(nums)

        # O(n log n)
        modified = dict(sorted(freq.items(), key = lambda x: x[1], reverse=True))

        # O(n) to extract all keys then O(k) to slice so O(n + k)
        return list(modified.keys())[:k]