class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            v1, v2 = numbers[l], numbers[r]

            if v1 + v2 == target:
                return [l + 1, r + 1]
            elif v1 + v2 > target:
                r -= 1
                continue
            else:
                l += 1
                continue
        
        return []