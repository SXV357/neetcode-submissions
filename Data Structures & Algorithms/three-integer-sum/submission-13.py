# solving based on NC video for O(1) space optimization

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # handle base cases
        n = len(nums)
        if n == 3:
            return [nums] if sum(nums) == 0 else []

        res = []
        nums.sort()

        for i in range(n - 2):
            j, k = i + 1, n - 1

            # if with nums[i] at position 1 we've already found a triplet
            # if we don't skip processing nums[i + 1] then we may end up
            # finding the same triplet which we want to avoid
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while j < k:
                added = nums[i] + nums[j] + nums[k]
                if added > 0:
                    k -= 1
                elif added < 0: 
                    j += 1
                else:
                    # we have found a triplet adding to 0
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        
        return res
