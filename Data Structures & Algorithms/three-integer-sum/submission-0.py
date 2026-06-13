from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        # handle base case
        if n == 3:
            return [nums] if sum(nums) == 0 else []
        
        seen = {}
        triplet_dic = defaultdict(int)

        for i, curr in enumerate(nums):
            j = i + 1
            while j < n:
                el = nums[j]
                curr_sum = curr + el

                if (0 - curr_sum in seen):
                    k = seen[0 - curr_sum]

                    # ensure i, j, k are distinct
                    if i != j and j != k and i != k:
                        vals = tuple([nums[i], nums[j], nums[k]])
                        triplet_dic[tuple(sorted(vals))] += 1
                else:
                    seen[el] = j
                
                j += 1
        
        res = []
        for key in triplet_dic.keys():
            res.append(list(key))
        
        return res