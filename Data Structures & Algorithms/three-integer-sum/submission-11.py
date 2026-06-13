from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        # handle base case
        if n == 3:
            return [nums] if sum(nums) == 0 else []
        
        res = []
        nums.sort()

        for i in range(n - 2):
            j, k = i + 1, n - 1

            while j < k:
                v1, v2, v3 = nums[i], nums[j], nums[k]

                if 0 == v1 + v2 + v3:
                    if i != j and j != k and i != k:
                        res.append([v1, v2, v3])
                        j += 1
                        k -= 1
                elif 0 > v1 + v2 + v3:
                    j += 1
                else:
                    k -= 1
                    
        unique = defaultdict(int)

        for triplet in res:
            modified = tuple(sorted(tuple(triplet)))
            unique[modified] += 1
        
        return list(list(key) for key in unique.keys())
            