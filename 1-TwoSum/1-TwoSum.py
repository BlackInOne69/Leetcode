# Last updated: 1/9/2026, 11:45:56 PM
class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, val in enumerate(nums):
            needed = target - val
            if needed in seen:
                return [seen[needed], i]
            seen[val] = i