# revisiting this one since couldn't come up with truly optimal solution 1st time

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # move towards an O(n) approach and remove sorting overhead

        '''
        sort of an array counting approach except we split into categories based
        on frequency

        max frequency an element could have is n and minimum is 1 so we have n
        buckets to categorize elements into based on frequency (elements with 
        freq of 1 go into bucket 1 and so on so naturally elements with highest
        frequency will end up in higher buckets that we can just do a pass over
        in reverse order)

        time = O(n), space = O(n)
        '''

        # O(n)
        freq = Counter(nums)
        n = len(nums)

        # O(n)
        buckets = [[] for _ in range(n)]

        # O(n) - at the most n keys
        for num, cnt in freq.items():
            buckets[cnt - 1].append(num)
        
        res = []
        count = 0

        # O(n) - more like an iterator but full pass is this much
        for bucket in reversed(buckets):
            for el in bucket:
                res.append(el)
                count += 1

                if count == k: return res