# Last updated: 1/31/2026, 8:20:05 PM
1class Solution:
2    def moveZeroes(self, nums: list[int]) -> None:
3        slow = 0 
4        
5        for fast in range(len(nums)):
6            if nums[fast] != 0:
7                nums[slow], nums[fast] = nums[fast], nums[slow]
8                slow += 1