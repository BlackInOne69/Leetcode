# Last updated: 1/9/2026, 11:45:48 PM
class Solution:
    def runningSum(self, nums):
        result = []
        total = 0
        for value in nums:
            total += value
            result.append(total)
        return result